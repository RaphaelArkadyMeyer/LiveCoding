

@@ comment:  What the instructor sees:

@@ begin hide
int main(int argv, char** argc) {

	printHello();

}
@@ end hide

@@ begin problem
@@ begin question printHello
@@ description: print "Hello, world!" to stdout;
@@ points: 100
@@ time: 36h

void printHello(){
	char* the_output = "Hello, world!";
@@ begin hide
	printf (the_output);
@@ end hide
}

@@ end question
@@ end problem







@@ comment:  What the student sees:



@@ begin question printHello
@@ Description: print "Hello, world!" to stdout;
@@ points: 100
@@ time: 36h

void printHello(){
	char* the_output = "Hello, world!";
	// code
}

@@ end question

