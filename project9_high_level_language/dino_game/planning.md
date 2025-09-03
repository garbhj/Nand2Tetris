# Possible Sprites

# Dinosaur Sprite Standing:
function void draw(int location) {
	var int memAddress; 
	let memAddress = 16384+location;
	// column 0
	do Memory.poke(memAddress, 32256);
	do Memory.poke(memAddress +32, -1280);
	do Memory.poke(memAddress +64, -256);
	do Memory.poke(memAddress +96, -256);
	do Memory.poke(memAddress +128, 3840);
	do Memory.poke(memAddress +160, 16257);
	do Memory.poke(memAddress +192, 2017);
	do Memory.poke(memAddress +224, 8179);
	do Memory.poke(memAddress +256, 6143);
	do Memory.poke(memAddress +288, 2047);
	do Memory.poke(memAddress +320, 2046);
	do Memory.poke(memAddress +352, 1020);
	do Memory.poke(memAddress +384, 440);
	do Memory.poke(memAddress +416, 304);
	do Memory.poke(memAddress +448, 272);
	do Memory.poke(memAddress +480, 816);
	return;
}

# Dinosaur Sprite Run 1:
function void draw(int location) {
	var int memAddress; 
	let memAddress = 16384+location;
	// column 0
	do Memory.poke(memAddress, 32256);
	do Memory.poke(memAddress +32, -1280);
	do Memory.poke(memAddress +64, -256);
	do Memory.poke(memAddress +96, -256);
	do Memory.poke(memAddress +128, 3840);
	do Memory.poke(memAddress +160, 16257);
	do Memory.poke(memAddress +192, 2017);
	do Memory.poke(memAddress +224, 8179);
	do Memory.poke(memAddress +256, 6143);
	do Memory.poke(memAddress +288, 2047);
	do Memory.poke(memAddress +320, 2046);
	do Memory.poke(memAddress +352, 1020);
	do Memory.poke(memAddress +384, 376);
	do Memory.poke(memAddress +416, 1840);
	do Memory.poke(memAddress +448, 16);
	do Memory.poke(memAddress +480, 48);
	return;
}

# Dinosaur Sprite Run 2:
function void draw(int location) {
	var int memAddress; 
	let memAddress = 16384+location;
	// column 0
	do Memory.poke(memAddress, 32256);
	do Memory.poke(memAddress +32, -1280);
	do Memory.poke(memAddress +64, -256);
	do Memory.poke(memAddress +96, -256);
	do Memory.poke(memAddress +128, 3840);
	do Memory.poke(memAddress +160, 16257);
	do Memory.poke(memAddress +192, 2017);
	do Memory.poke(memAddress +224, 8179);
	do Memory.poke(memAddress +256, 6143);
	do Memory.poke(memAddress +288, 2047);
	do Memory.poke(memAddress +320, 2046);
	do Memory.poke(memAddress +352, 1020);
	do Memory.poke(memAddress +384, 408);
	do Memory.poke(memAddress +416, 304);
	do Memory.poke(memAddress +448, 256);
	do Memory.poke(memAddress +480, 768);
	return;
}

# Dinosaur Sprite Crouch 1:
function void draw(int location) {
	var int memAddress; 
	let memAddress = 16384+location;
	// column 0
	do Memory.poke(memAddress, 31745);
	do Memory.poke(memAddress +32, -2317);
	do Memory.poke(memAddress +64, -1);
	do Memory.poke(memAddress +96, -1);
	do Memory.poke(memAddress +128, 4094);
	do Memory.poke(memAddress +160, 16380);
	do Memory.poke(memAddress +192, 1016);
	do Memory.poke(memAddress +224, 1784);
	do Memory.poke(memAddress +256, 88);
	do Memory.poke(memAddress +288, 456);
	do Memory.poke(memAddress +320, 24);
	return;
}

# Dinosaur Sprite Crouch 2:
function void draw(int location) {
	var int memAddress; 
	let memAddress = 16384+location;
	// column 0
	do Memory.poke(memAddress, 31745);
	do Memory.poke(memAddress +32, -2317);
	do Memory.poke(memAddress +64, -1);
	do Memory.poke(memAddress +96, -1);
	do Memory.poke(memAddress +128, 4094);
	do Memory.poke(memAddress +160, 16380);
	do Memory.poke(memAddress +192, 1016);
	do Memory.poke(memAddress +224, 1784);
	do Memory.poke(memAddress +256, 200);
	do Memory.poke(memAddress +288, 88);
	do Memory.poke(memAddress +320, 192);
	return;
}

# Note: Cacti are referenced two blocks above the dinosaur
# Cactus Single Large
function void draw(int location) {
	var int memAddress; 
	let memAddress = 16384+location;
	// column 0
	do Memory.poke(memAddress, 32);
	do Memory.poke(memAddress +32, 112);
	do Memory.poke(memAddress +64, 112);
	do Memory.poke(memAddress +96, 112);
	do Memory.poke(memAddress +128, 1648);
	do Memory.poke(memAddress +160, 1650);
	do Memory.poke(memAddress +192, 1651);
	do Memory.poke(memAddress +224, 1651);
	do Memory.poke(memAddress +256, 1651);
	do Memory.poke(memAddress +288, 1907);
	do Memory.poke(memAddress +320, 1023);
	do Memory.poke(memAddress +352, 254);
	do Memory.poke(memAddress +384, 112);
	do Memory.poke(memAddress +416, 112);
	do Memory.poke(memAddress +448, 112);
	do Memory.poke(memAddress +480, 112);
	do Memory.poke(memAddress +512, 112);
	do Memory.poke(memAddress +544, 120);
	return;
}

# Cactus Single Small
function void draw(int location) {
	var int memAddress; 
	let memAddress = 16384+location;
	// column 0
	do Memory.poke(memAddress, 16);
	do Memory.poke(memAddress +32, 24);
	do Memory.poke(memAddress +64, 24);
	do Memory.poke(memAddress +96, 24);
	do Memory.poke(memAddress +128, 88);
	do Memory.poke(memAddress +160, 217);
	do Memory.poke(memAddress +192, 219);
	do Memory.poke(memAddress +224, 123);
	do Memory.poke(memAddress +256, 27);
	do Memory.poke(memAddress +288, 30);
	do Memory.poke(memAddress +320, 24);
	do Memory.poke(memAddress +352, 24);
	do Memory.poke(memAddress +384, 24);
	do Memory.poke(memAddress +416, 24);
	return;
}

# Cactus Double Large
function void draw(int location) {
	var int memAddress; 
	let memAddress = 16384+location;
	// column 0
	do Memory.poke(memAddress, 32);
	do Memory.poke(memAddress +32, 112);
	do Memory.poke(memAddress +64, 112);
	do Memory.poke(memAddress +96, 8304);
	do Memory.poke(memAddress +128, 13936);
	do Memory.poke(memAddress +160, 13938);
	do Memory.poke(memAddress +192, 13939);
	do Memory.poke(memAddress +224, 13939);
	do Memory.poke(memAddress +256, 13939);
	do Memory.poke(memAddress +288, -2189);
	do Memory.poke(memAddress +320, -7169);
	do Memory.poke(memAddress +352, 254);
	do Memory.poke(memAddress +384, 112);
	do Memory.poke(memAddress +416, 112);
	do Memory.poke(memAddress +448, 112);
	do Memory.poke(memAddress +480, 112);
	do Memory.poke(memAddress +512, 112);
	do Memory.poke(memAddress +544, -32648);
	// column 1
	do Memory.poke(memAddress +1, 2);
	do Memory.poke(memAddress +33, 7);
	do Memory.poke(memAddress +65, 7);
	do Memory.poke(memAddress +97, 7);
	do Memory.poke(memAddress +129, 7);
	do Memory.poke(memAddress +161, 39);
	do Memory.poke(memAddress +193, 103);
	do Memory.poke(memAddress +225, 103);
	do Memory.poke(memAddress +257, 103);
	do Memory.poke(memAddress +289, 103);
	do Memory.poke(memAddress +321, 103);
	do Memory.poke(memAddress +353, 55);
	do Memory.poke(memAddress +385, 31);
	do Memory.poke(memAddress +417, 15);
	do Memory.poke(memAddress +449, 7);
	do Memory.poke(memAddress +481, 7);
	do Memory.poke(memAddress +513, 7);
	do Memory.poke(memAddress +545, 7);
	return;
}

# Cactus Double Small
function void draw(int location) {
	var int memAddress; 
	let memAddress = 16384+location;
	// column 0
	do Memory.poke(memAddress, 4112);
	do Memory.poke(memAddress +32, 12312);
	do Memory.poke(memAddress +64, 12312);
	do Memory.poke(memAddress +96, 13336);
	do Memory.poke(memAddress +128, 13912);
	do Memory.poke(memAddress +160, 14041);
	do Memory.poke(memAddress +192, -17189);
	do Memory.poke(memAddress +224, -20357);
	do Memory.poke(memAddress +256, -20453);
	do Memory.poke(memAddress +288, -4066);
	do Memory.poke(memAddress +320, 12312);
	do Memory.poke(memAddress +352, 12312);
	do Memory.poke(memAddress +384, 12312);
	do Memory.poke(memAddress +416, 12312);
	// column 1
	do Memory.poke(memAddress +161, 1);
	do Memory.poke(memAddress +193, 1);
	do Memory.poke(memAddress +225, 1);
	do Memory.poke(memAddress +257, 1);
	do Memory.poke(memAddress +289, 0);
	do Memory.poke(memAddress +321, 0);
	do Memory.poke(memAddress +353, 0);
	do Memory.poke(memAddress +385, 0);
	do Memory.poke(memAddress +417, 0);
	return;
}

# Cactus Triple Small
function void draw(int location) {
	var int memAddress; 
	let memAddress = 16384+location;
	// column 0
	do Memory.poke(memAddress, 4096);
	do Memory.poke(memAddress +32, 12304);
	do Memory.poke(memAddress +64, -19432);
	do Memory.poke(memAddress +96, -18919);
	do Memory.poke(memAddress +128, -18789);
	do Memory.poke(memAddress +160, -18725);
	do Memory.poke(memAddress +192, -2337);
	do Memory.poke(memAddress +224, -290);
	do Memory.poke(memAddress +256, 15608);
	do Memory.poke(memAddress +288, 12408);
	do Memory.poke(memAddress +320, 12312);
	do Memory.poke(memAddress +352, 12312);
	do Memory.poke(memAddress +384, 12312);
	do Memory.poke(memAddress +416, 14364);
	// column 1
	do Memory.poke(memAddress +33, 32);
	do Memory.poke(memAddress +65, 97);
	do Memory.poke(memAddress +97, 353);
	do Memory.poke(memAddress +129, 869);
	do Memory.poke(memAddress +161, 877);
	do Memory.poke(memAddress +193, 877);
	do Memory.poke(memAddress +225, 1004);
	do Memory.poke(memAddress +257, 492);
	do Memory.poke(memAddress +289, 124);
	do Memory.poke(memAddress +321, 120);
	do Memory.poke(memAddress +353, 96);
	do Memory.poke(memAddress +385, 96);
	do Memory.poke(memAddress +417, 224);
	return;
}

# Cactus Multiple Large
function void draw(int location) {
	var int memAddress; 
	let memAddress = 16384+location;
	// column 0
	do Memory.poke(memAddress, 32);
	do Memory.poke(memAddress +32, 112);
	do Memory.poke(memAddress +64, 112);
	do Memory.poke(memAddress +96, -32656);
	do Memory.poke(memAddress +128, -27024);
	do Memory.poke(memAddress +160, -18830);
	do Memory.poke(memAddress +192, -18829);
	do Memory.poke(memAddress +224, -18829);
	do Memory.poke(memAddress +256, -18829);
	do Memory.poke(memAddress +288, -18573);
	do Memory.poke(memAddress +320, -19457);
	do Memory.poke(memAddress +352, -7938);
	do Memory.poke(memAddress +384, -16272);
	do Memory.poke(memAddress +416, -32656);
	do Memory.poke(memAddress +448, -32656);
	do Memory.poke(memAddress +480, -32656);
	do Memory.poke(memAddress +512, -32656);
	do Memory.poke(memAddress +544, -32648);
	// column 1
	do Memory.poke(memAddress +1, 8192);
	do Memory.poke(memAddress +33, 28672);
	do Memory.poke(memAddress +65, 28673);
	do Memory.poke(memAddress +97, 28673);
	do Memory.poke(memAddress +129, 28929);
	do Memory.poke(memAddress +161, 29449);
	do Memory.poke(memAddress +193, 29453);
	do Memory.poke(memAddress +225, 29485);
	do Memory.poke(memAddress +257, 29549);
	do Memory.poke(memAddress +289, 30567);
	do Memory.poke(memAddress +321, 32355);
	do Memory.poke(memAddress +353, -663);
	do Memory.poke(memAddress +385, -3735);
	do Memory.poke(memAddress +417, 29033);
	do Memory.poke(memAddress +449, 29177);
	do Memory.poke(memAddress +481, 28769);
	do Memory.poke(memAddress +513, 28769);
	do Memory.poke(memAddress +545, 28769);
	// column 2
	do Memory.poke(memAddress +130, 2);
	do Memory.poke(memAddress +162, 6);
	do Memory.poke(memAddress +194, 6);
	do Memory.poke(memAddress +226, 6);
	do Memory.poke(memAddress +258, 6);
	do Memory.poke(memAddress +290, 6);
	do Memory.poke(memAddress +322, 7);
	do Memory.poke(memAddress +354, 3);
	do Memory.poke(memAddress +386, 1);
	do Memory.poke(memAddress +418, 0);
	do Memory.poke(memAddress +450, 0);
	do Memory.poke(memAddress +482, 0);
	do Memory.poke(memAddress +514, 0);
	do Memory.poke(memAddress +546, 0);
	return;
}
