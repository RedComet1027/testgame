coinSprite: Sprite = None
effects.star_field.start_screen_effect()
playerSprite = sprites.create(img("""
        . . . . . f f f f . . . . . 
            . . . f f 5 5 5 5 f f . . . 
            . . f 5 5 5 5 5 5 5 5 f . . 
            . f 5 5 5 5 5 5 5 5 5 5 f . 
            . f 5 5 5 d b b d 5 5 5 f . 
            f 5 5 5 b 4 4 4 4 b 5 5 5 f 
            f 5 5 c c 4 4 4 4 c c 5 5 f 
            f b b f b f 4 4 f b f b b f 
            f b b 4 1 f d d f 1 4 b b f 
            . f b f d d d d d d f b f . 
            . f e f e 4 4 4 4 e f e f . 
            . e 4 f 6 9 9 9 9 6 f 4 e . 
            . 4 d c 9 9 9 9 9 9 c d 4 . 
            . 4 f b 3 b 3 b 3 b b f 4 . 
            . . f f 3 b 3 b 3 3 f f . . 
            . . . . f f b b f f . . . .
    """),
    SpriteKind.player)
controller.move_sprite(playerSprite)
playerSprite.set_flag(SpriteFlag.STAY_IN_SCREEN, True)
for index in range(4):
    coinSprite = sprites.create(img("""
            . . . b b b . . 
                    . . b 5 5 5 b . 
                    . b 5 d 3 d 5 b 
                    . b 5 1 5 3 5 b 
                    . c d 1 5 3 5 c 
                    . c d d 1 d 5 c 
                    . . f d d d f . 
                    . . . f f f . .
        """),
        SpriteKind.enemy)
    coinSprite.x = randint(10, scene.screen_width() - 10)
    coinSprite.y = randint(10, scene.screen_height() - 10)