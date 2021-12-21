from typing import Iterable


RAW = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""

pairs = {"{": "}", "(": ")", "<": ">", "[": "]"}
scores = {")": 3, "]": 57, "}": 1197, ">": 25137, "OK": 0}
ac_score = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def is_corrupted(s: str) -> str:
    stack = []
    for c in s:
        if c in pairs:
            stack.append(pairs[c])
        else:
            if stack.pop() != c:
                return c
    return "OK"


def complete(s: str) -> str:
    if is_corrupted(s) != "OK":
        return ""
    stack = []
    for c in s:
        if c in pairs:
            stack.append(pairs[c])
        else:
            if stack.pop() != c:
                raise RuntimeError("Cannot complete corrupted string")
    out = ""
    while stack:
        out += stack.pop()
    return out


def total_score(indata: Iterable[str]) -> int:
    total = 0
    for s in indata:
        total += scores[is_corrupted(s)]
    return total


def autocomplete_score(s: str):
    s = complete(s)
    score = 0
    for c in s:
        score *= 5
        score += ac_score[c]
    return score


def autocomplete_total_score(indata: Iterable[str]) -> int:
    scores = []
    for s in indata:
        score = autocomplete_score(s)
        if score > 0:
            scores.append(score)
    print(sorted(scores))
    # 0 based indexing so the middle value is (n-1)/2 i.e. 5 -> 2, 7 -> 3 etc
    return sorted(scores)[(len(scores) - 1) // 2]


assert total_score(RAW.splitlines()) == 26397

indata = open("day10.txt").read()
print(total_score(indata.splitlines()))
print(autocomplete_total_score(indata.splitlines()))

# for line in RAW.splitlines():
#     print(line, " --> ", complete(line))
#     print(autocomplete_score(line))
# print(autocomplete_total_score(RAW.splitlines()))
