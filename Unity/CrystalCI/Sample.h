#pragma once
#ifdef UNITY_EXPORTS
#define SAMPLE_API __declspec(dllexport)
#else
#define SAMPLE_API __declspec(dllimport)
#endif

extern "C" {
	SAMPLE_API void CreateCommand(const char* str);

	SAMPLE_API void CreatePhysicsCommand(const char* str);

	SAMPLE_API void SetArgInt(const char* name, int i);

	SAMPLE_API void SetArgFloat(const char* name, float f);

	SAMPLE_API void SetArgDouble(const char* name, double d);

	SAMPLE_API void SetArgString(const char* name, const char* str);

	SAMPLE_API void SetArgVector3ds(const char* name, float* values);

	SAMPLE_API int Execute();

	SAMPLE_API int GetResultInt(const char* name);
}