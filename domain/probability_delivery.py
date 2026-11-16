"""概率语音保留宿主分段，只拆开同段内的正文、提及与表情发送。"""

from copy import deepcopy
from typing import Any, Dict, List, Optional, Tuple

import base64
import hashlib
import json

SPEECH_SEGMENTS = {"text", "at", "reply", "emoji"}


def speech_text(segments: List[Dict[str, Any]]) -> Optional[str]:
    """图片等媒体段沿用宿主发送；提及、引用与表情不参与朗读。"""
    if any(segment.get("type") not in SPEECH_SEGMENTS for segment in segments):
        return None
    texts = [segment["data"] for segment in segments if segment.get("type") == "text"]
    return "".join(texts).strip() or None


def delivery_attachments(
    segments: List[Dict[str, Any]],
) -> Tuple[List[List[Dict[str, Any]]], List[List[Dict[str, Any]]]]:
    """按正文位置分出前后附件批次，同类型相邻段保留为一组，字段原样复制。"""
    before: List[List[Dict[str, Any]]] = []
    after: List[List[Dict[str, Any]]] = []
    body_started = False
    for segment in segments:
        kind = segment.get("type")
        if kind == "text":
            body_started = body_started or bool(segment["data"].strip())
            continue
        if kind in {"reply", "voice"}:
            continue
        groups = after if body_started else before
        if groups and groups[-1][-1]["type"] == kind:
            groups[-1].append(deepcopy(segment))
        else:
            groups.append([deepcopy(segment)])
    return before, after


def batch_text(segments: List[Dict[str, Any]]) -> str:
    """发送摘要取自本批正文，媒体二进制与描述继续由宿主处理。"""
    return "".join(segment["data"] for segment in segments if segment.get("type") == "text")


def source_key(segments: List[Dict[str, Any]]) -> str:
    """同音频并发回复按正文与原生附件区分，引用由发送阶段单独判定。"""
    values = []
    for segment in segments:
        kind = segment.get("type")
        if kind == "text":
            values.append((kind, segment["data"]))
        elif kind == "at":
            values.append((kind, segment["data"]["target_user_id"]))
        elif kind == "emoji":
            binary_hash = str(segment.get("hash") or "")
            if not binary_hash and segment.get("binary_data_base64"):
                binary_hash = hashlib.sha256(base64.b64decode(segment["binary_data_base64"], validate=True)).hexdigest()
            values.append((kind, binary_hash, segment["data"]))
    return hashlib.sha256(json.dumps(values, ensure_ascii=False).encode("utf-8")).hexdigest()
