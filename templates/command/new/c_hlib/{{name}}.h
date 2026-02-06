/* {{name}}.h - <description>
 */

#ifndef {{name | upper}}_H
#define {{name | upper}}_H

#define {{name | upper}}_VERSION "{{version}}"

/* HEADER */

#endif /* PLM_BS_H */

#ifdef {{name | upper}}_IMPLEMENTATION
#undef {{name | upper}}_IMPLEMENTATION

/* IMPLEMENTATION */

#endif /* {{name | upper}}_IMPLEMENTATION */

#ifdef {{name | upper}}_TEST

#include <stdio.h>
#include <assert.h>

#ifndef {{name | upper}}_TEST_VERBOSE
# define {{name | upper}}_TEST_VERBOSE 0
#endif

/* TESTS */

#endif /* {{name | upper}}_TEST */
