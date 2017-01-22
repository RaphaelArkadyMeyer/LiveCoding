
@@ begin hide
main:
	mov r1, r0
	b fibbonacci
@@ end hide

fibonacci:
	push  {r1-r3}
	mov   r1,  #0
	mov   r2,  #1
@@ begin question fibbonacci
@@ description: return the nth fibbonacci number, where n is stored in r0
@@ points: 40
@@ time: 30 minutes

fibloop:
	mov   r3,  r2
	add   r2,  r1,  r2
	mov   r1,  r3
	sub   r0,  r0,  #1
	cmp   r0,  #1
	bne   fibloop

	mov   r0,  r2
@@ end question
	pop   {r1-r3}
	mov   pc,  lr
