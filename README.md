# stereo_bot
`stereo_bot_` it's a simple robot designed for stereo vision experiments inside ROS. It consists on a base fixed to the world, a neck, and a head with two paralel cameras.

The cameras can be customized in the file `stereo_bot_description/stereo_bot.gazebo`. They are published on the topics
* `/stereo_bot/camera_l/image_raw`
* `/stereo_bot/camera_r/image_raw`

The head of `stereo_bot` is fixed to the neck. The neck can rotate from -PI/2 to PI/2 as a revolute joint.
