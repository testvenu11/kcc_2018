class GameData:
	debug_mode = False

	GRAPHICS_ASTEROID_FILENAME = "../assets/graphics/asteroid.png"
	GRAPHICS_EARTH_FILENAME = "../assets/graphics/earth.png"
	GRAPHICS_SKY_FILENAME = "../assets/graphics/space.png"
	GRAPHICS_GAME_OVER_TEXT = "../assets/graphics/gameover.png"
	GRAPHICS_PRES_SPACE_TEXT = "../assets/graphics/pressspace.png"
	GRAPHICS_MISSILE1_FILENAME = "../assets/graphics/missile1.png"
	GRAPHICS_MISSILE2_FILENAME = "../assets/graphics/missile2.png"

	SOUND_ON = True
	MUSIC_ON = True
	SOUND_GUN_FILENAME = "../assets/sounds/gun1.wav"
	SOUND_MISSILE_FILENAME = "../assets/sounds/missile.wav"
	SOUND_MULTIMISSILE_FILENAME = "../assets/sounds/multimissile.wav"
	SOUND_ASTEROID_COLLISION_FILENAME = "../assets/sounds/aster-collide1.wav"
	SOUND_ASTEROID_BREAKUP_FILENAME	= "../assets/sounds/earth-collide-3.wav"
	SOUND_EARTH_COLLISION0_FILENAME = "../assets/sounds/earth-collide-0.wav"
	SOUND_EARTH_COLLISION1_FILENAME = "../assets/sounds/earth-collide-1.wav"
	SOUND_EARTH_COLLISION2_FILENAME = "../assets/sounds/earth-collide-2.wav"
	SOUND_EARTH_COLLISION3_FILENAME = "../assets/sounds/earth-collide-3.wav"
	SOUND_EARTH_COLLISION4_FILENAME = "../assets/sounds/earth-collide-4.wav"
	SOUND_BACKGROUND_FILENAME = "../assets/sounds/background.mp3"

	ASTEROID_LEVEL0_PROBABILITY = 1
	ASTEROID_LEVEL1_PROBABILITY = 25
	ASTEROID_LEVEL2_PROBABILITY = 50
	ASTEROID_LEVEL3_PROBABILITY = 75
	ASTEROID_LEVEL4_PROBABILITY = 100

	MAX_ASTEROIDS = 10
	ASTEROID_SHARD_MULTIPLIER = 2.0
	NEW_ASTEROID_FREQUENCY = 3000

	WEAPON_GUN_COOLDOWN = 30
	WEAPON_GUN_DAMAGE = 1
	WEAPON_GUN_SPEED = 3.0
	
	WEAPON_MULTIGUN_COOLDOWN = 1500
	WEAPON_MULTIGUN_DAMAGE = 1
	WEAPON_MULTIGUN_SHOT_COUNT = 20
	WEAPON_MULTIGUN_SPREAD = 45
	WEAPON_MULTIGUN_FAN = 1.6
	WEAPON_MULTIGUN_SPEED_MULTIPLIER = 1.5

	WEAPON_MISSILE_COOLDOWN = 175
	WEAPON_MISSILE_DAMAGE = 100
	WEAPON_MISSILE_SPEED = 0.2
	WEAPON_MISSILE_ACCELERATION = 1.4
	WEAPON_MISSILE_MAX_SPEED = 20.0

	WEAPON_MULTIMISSILE_COOLDOWN = 4000
	WEAPON_MULTIMISSILE_DAMAGE = 50
	WEAPON_MULTIMISSILE_SPEED = 0.5
	WEAPON_MULTIMISSILE_ACCELERATION = 1.5
	WEAPON_MULTIMISSILE_MAX_SPEED = 4.0
	WEAPON_MULTIMISSILE_SHOT_COUNT = 10
	WEAPON_MULTIMISSILE_FAN = 6.0
