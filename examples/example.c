@@ begin hide
int main(int argv, char** argc) {

	printHello();

}
@@ end hide


@@ begin question printHello
@@ description: print "Hello, world!" to stdout;
@@ points: 100
@@ time: 36h
void printHello(){
	char* the_output = "Hello, world!";
	printf (the_output);
}
@@ end question
