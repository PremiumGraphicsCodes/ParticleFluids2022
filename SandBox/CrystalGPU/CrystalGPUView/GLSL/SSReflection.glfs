#version 150
in vec2 texCoord;
out vec4 fragColor;
uniform mat4 projectionMatrix;
uniform vec3 eyePosition;
uniform sampler2D depthTex;
uniform sampler2D normalTex;
uniform samplerCube cubeMapTex;
float getDepth(vec2 tCoord){
	return texture2D(depthTex, tCoord).r;
}
vec3 uvToEye(vec2 tCoord, float depth) {
	vec4 clippingPosition = vec4(tCoord, depth, 1.0);
	vec4 viewPosition = inverse(projectionMatrix) * clippingPosition;
	return viewPosition.xyz / viewPosition.w;
}
vec3 getEyePosition(vec2 texCoord){
	float depth = getDepth(texCoord);
	return uvToEye(texCoord, depth);
}
void main(void) {
	float depth = getDepth(texCoord);
	if(depth < 0.01) {
		fragColor = vec4(0.0, 0.0, 0.0, 0.0);
		return;
	}
	vec3 normal = texture2D(normalTex, texCoord).rgb;
	vec3 position = getEyePosition(texCoord);
	vec3 worldView = normalize( eyePosition - position );
	float innerProduct = dot(-worldView, normal);
	float fresnelBias = pow( (1.0-1.33) /(1.0+1.33), 2);
	float fresnel = fresnelBias + ( 1.0 - fresnelBias ) * pow(1.0 - innerProduct, 5);
	vec3 reflectDir = reflect(-worldView, normal);
	vec3 refractDir = refract(-worldView, normal, 1.33);
	vec4 reflectColor = texture(cubeMapTex, reflectDir);
	vec4 refractColor = texture(cubeMapTex, refractDir);
	fragColor = mix( reflectColor,refractColor,fresnel);
	fragColor = reflectColor;
//	fragColor = vec4(fresnel);
	fragColor.a = 1.0f;
}