#version 150
uniform sampler2D surfaceTexture;
uniform sampler2D reflectionTexture;
uniform sampler2D refractionTexture;
uniform sampler2D absorptionTexture;
uniform sampler2D backgroundTexture;
in vec2 texCoord;
out vec4 fragColor;
void main(void) {
	vec4 surfaceColor = texture2D(surfaceTexture, texCoord);
	vec4 reflectionColor = texture2D(reflectionTexture, texCoord);
	vec4 refractionColor = texture2D(refractionTexture, texCoord);
	vec4 absorptionColor = texture2D(absorptionTexture, texCoord);
	vec4 bgColor = texture2D(backgroundTexture, texCoord);
	if(absorptionColor.a < 0.01) {
		fragColor = bgColor;
		return;
	}else{
		fragColor = mix( absorptionColor, surfaceColor *0.5 + reflectionColor * 0.5, 1.0-absorptionColor.a);
	}
}