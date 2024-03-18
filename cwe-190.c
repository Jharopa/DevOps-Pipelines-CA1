int main(int argc, char** argv) {
	char buffer[20];
	fgets(buffer, 20, stdin);

	int num = atoi(buffer);
	// BAD: may overflow if input is very large
	int scaled = num + 1000;
}