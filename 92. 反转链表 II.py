class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if head == None:
            return head
        if head.next == None:
            return head
        if m == n:
            return head
        
        new_head = head

        #找到截取位置
        count = 1
        while count<m:
            temp = head
            head =head.next
            count += 1
        if count == 1:
            return self.reverse_list(head,n-m+1)
        else:
            temp.next = self.reverse_list(head,n-m+1)
            return new_head
            '''
            while new_head:
                print(new_head.val)
                new_head = new_head.next
            '''
    def reverse_list(self,head,k):
        head1 = head
        head2 = head1.next
        count = 1
        while count<k:
            head.next = head2.next
            head2.next = head1
            head1 = head2
            head2 = head.next
            count += 1
            print(count,head1.val)
        return head1
        