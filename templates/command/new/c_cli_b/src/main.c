#include <stdlib.h>
#include <stddef.h>

#include "version.h"

typedef struct Parameters_ {
	int version;
} Parameters;

int main(int argc, char **argv)
{
	Parameters params;

	/* Default arguments */
	params.version = 0;
	/* ----------------- */

	char *doc = "<description here>";

	if(params.version){
		printf("Version: %s\n", VERSION);
	}

	return EXIT_SUCCESS;
}
