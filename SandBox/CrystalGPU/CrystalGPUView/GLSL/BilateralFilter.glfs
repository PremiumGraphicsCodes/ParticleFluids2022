#version 150
uniform sampler2D tex;
uniform float width;
uniform float height;
in vec2 texCoord;
out vec4 fragColor;
void main(void) {
	float sum = 0;
	float wsum = 0;
	float filterRadius = 5;
	float blurScale = 1;
	float blurDepthFalloff = 1.0;
	float depth = texture2D(tex, texCoord).r;
	for(float x = -filterRadius; x <= filterRadius; x+= 1.0){
		for(float y = -filterRadius; y <= filterRadius; y+= 1.0){
			float dxx = (x/width);
			float dyy = (y/height);
			vec2 offset = vec2(dxx,dyy);
			float sample = texture2D(tex, texCoord + offset ).r;
			float r = sqrt(dxx * dxx + dyy * dyy) * blurScale;
			float w = exp(-r*r);
			float r2 = (sample-depth) * blurDepthFalloff;
			float g = exp(-r2*r2);
			sum += sample * w * g;
			wsum += w * g;
		}
	}
	if(wsum > 0.0) {
		sum /= wsum;
	}
	fragColor = vec4(sum);
}