def runner_solution(head: ListNode) -> bool:
    # 1. slow runner, fast runner head로 초기화
    slow, fast = head, head
    rev = None # reversed linked list

    # reversed linked list 구성
    while fast and fast.next:
        # 여기서 fast runner는 linked list의 절반 지점을 체크하기 위하여 사용
        fast = fast.next.next  # 2 step 이동
        rev, rev.next, slow = slow, rev, slow.next # reversed linked list 구성

    if fast:
        slow = slow.next  # 홀수 길이의 linked list 받은 경우를 위해

    while rev and rev.val == slow.val:
        rev, slow = rev.next, slow.next
    return not rev
