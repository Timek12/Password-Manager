# CMAKE generated file: DO NOT EDIT!
# Generated by "MinGW Makefiles" Generator, CMake Version 3.25

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

SHELL = cmd.exe

# The CMake executable.
CMAKE_COMMAND = "C:\Program Files\JetBrains\CLion 2023.1.1\bin\cmake\win\x64\bin\cmake.exe"

# The command to remove a file.
RM = "C:\Program Files\JetBrains\CLion 2023.1.1\bin\cmake\win\x64\bin\cmake.exe" -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = C:\Users\HP\CLionProjects\Security_System

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = C:\Users\HP\CLionProjects\Security_System\cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/Security_System.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/Security_System.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/Security_System.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/Security_System.dir/flags.make

CMakeFiles/Security_System.dir/main.c.obj: CMakeFiles/Security_System.dir/flags.make
CMakeFiles/Security_System.dir/main.c.obj: C:/Users/HP/CLionProjects/Security_System/main.c
CMakeFiles/Security_System.dir/main.c.obj: CMakeFiles/Security_System.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=C:\Users\HP\CLionProjects\Security_System\cmake-build-debug\CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/Security_System.dir/main.c.obj"
	C:\Users\HP\mingw64\bin\x86_64-w64-mingw32-gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT CMakeFiles/Security_System.dir/main.c.obj -MF CMakeFiles\Security_System.dir\main.c.obj.d -o CMakeFiles\Security_System.dir\main.c.obj -c C:\Users\HP\CLionProjects\Security_System\main.c

CMakeFiles/Security_System.dir/main.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/Security_System.dir/main.c.i"
	C:\Users\HP\mingw64\bin\x86_64-w64-mingw32-gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E C:\Users\HP\CLionProjects\Security_System\main.c > CMakeFiles\Security_System.dir\main.c.i

CMakeFiles/Security_System.dir/main.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/Security_System.dir/main.c.s"
	C:\Users\HP\mingw64\bin\x86_64-w64-mingw32-gcc.exe $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S C:\Users\HP\CLionProjects\Security_System\main.c -o CMakeFiles\Security_System.dir\main.c.s

# Object files for target Security_System
Security_System_OBJECTS = \
"CMakeFiles/Security_System.dir/main.c.obj"

# External object files for target Security_System
Security_System_EXTERNAL_OBJECTS =

Security_System.exe: CMakeFiles/Security_System.dir/main.c.obj
Security_System.exe: CMakeFiles/Security_System.dir/build.make
Security_System.exe: CMakeFiles/Security_System.dir/linkLibs.rsp
Security_System.exe: CMakeFiles/Security_System.dir/objects1
Security_System.exe: CMakeFiles/Security_System.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=C:\Users\HP\CLionProjects\Security_System\cmake-build-debug\CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable Security_System.exe"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles\Security_System.dir\link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/Security_System.dir/build: Security_System.exe
.PHONY : CMakeFiles/Security_System.dir/build

CMakeFiles/Security_System.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles\Security_System.dir\cmake_clean.cmake
.PHONY : CMakeFiles/Security_System.dir/clean

CMakeFiles/Security_System.dir/depend:
	$(CMAKE_COMMAND) -E cmake_depends "MinGW Makefiles" C:\Users\HP\CLionProjects\Security_System C:\Users\HP\CLionProjects\Security_System C:\Users\HP\CLionProjects\Security_System\cmake-build-debug C:\Users\HP\CLionProjects\Security_System\cmake-build-debug C:\Users\HP\CLionProjects\Security_System\cmake-build-debug\CMakeFiles\Security_System.dir\DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/Security_System.dir/depend

