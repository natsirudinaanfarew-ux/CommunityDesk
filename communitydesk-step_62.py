# === Stage 62: Add simple scoring or priority recommendation logic ===
# Project: CommunityDesk
def recommend_volunteer(request: dict, volunteers: list) -> int:
    """Return an index into 'volunteers' that best matches a request.

    Scoring is simple and additive so the logic stays readable:
      +3  if the volunteer's skills overlap with required_skills (case-insensitive),
      +2  if the volunteer has done similar past_requests,
      -10 if the requested category differs from any of the volunteer's categories.

    Volunteers are returned in descending score order; ties keep original order.
    """
    def _match(text: str) -> bool:
        return text.lower() in req_skills_lower

    req_skills_lower = {s.strip().lower() for s in request.get("required_skills", [])}
    past_requests = request.get("past_requests", [])

    scores = []
    for i, v in enumerate(volunteers):
        v_skills = {s.strip().lower() for s in v.get("skills", [])}
        v_categories = [c.strip().lower() for c in v.get("categories", [])]
        past_v_requests = v.get("past_requests", [])

        skill_hit = len(v_skills & req_skills_lower) / max(len(req_skills_lower), 1) if req_skills_lower else 0.0
        past_match = sum(1 for pr in past_v_requests if _match(pr)) / max(len(past_v_requests), 1) if past_v_requests else 0.0

        score = int(skill_hit * 3 + past_match * 2 - (not any(_match(c) for c in v_categories) and len(v_categories)))
        scores.append((score, i))

    return max(scores, key=lambda x: x[0])[1] if scores else -1
