

fibonacci:
	push  {r1-r3}
	mov   r1,  #0
	mov   r2,  #1
@@ begin question fibbonacci
@@ description: return the nth fibbonacci number, where n is stored in r0
@@ points: 40
@@ time: 30 minutes










@@ end question
	pop   {r1-r3}
	mov   pc,  lr
