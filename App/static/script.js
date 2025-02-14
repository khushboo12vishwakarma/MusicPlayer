var audio = {
    init: function() {
        var $that = this;
        $(document).ready(function() {
            $that.components.media();
        });
    },
    components: {
        media: function() {
            var media = $('audio.fc-media');
            if (media.length) {
                media.mediaelementplayer({
                    audioHeight: 40,
                    features: ['playpause', 'current', 'duration', 'progress', 'volume', 'tracks', 'fullscreen'],
                    alwaysShowControls: true,
                    timeAndDurationSeparator: '<span></span>',
                    iPadUseNativeControls: true,
                    iPhoneUseNativeControls: true,
                    AndroidUseNativeControls: true,
                    success: function(player, node) {
                        syncLyrics(player, node);
                    }
                });
            }
        }
    }
};
audio.init();


