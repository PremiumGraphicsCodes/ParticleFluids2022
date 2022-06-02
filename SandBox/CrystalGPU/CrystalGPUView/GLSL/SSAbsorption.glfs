#version 150
uniform sampler2D volumeTex;
in vec2 texCoord;
out vec4 fragColor;
void main(void) {
	float volume = texture2D(volumeTex, texCoord).a;
	if(volume < 0.01 ) {
		fragColor.rgb = vec3(0.0, 0.0, 0.0);
		fragColor.a = 0.0;
		return;
	}
	float k = 0.1;
	fragColor.rgb = exp(-k*volume) * vec3(5/255.0, 102/255.0, 255/255.0);
	fragColor.rgb += vec3(0.0, 0.0, 0.0);
	fragColor.a = volume;
}