# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        head1=head
        if head==None or head.next==None:
            return head
        current=head
        head1=head1.next
        top=head1
        if top.next==None:
            return head
        while(current.next!=None and head1.next!=None):

            current.next=head1.next
            current=current.next
            head1.next=current.next
            head1=head1.next
        current.next=top
        return head
