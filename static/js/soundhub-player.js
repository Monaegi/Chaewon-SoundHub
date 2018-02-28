function playerDuration(audio) {
    var player_total_duration = $("#player-total-duration");
    player_total_duration.text(format_time(audio.duration));
}

function playerCurrentTime(audio) {
    var player_current_time = $("#player-current-time");
    $(audio).on("timeupdate", function() {
        player_current_time.text(format_time(audio.currentTime))
    });

}

// 트랙 쪽에서 버튼을 눌렀을 때 플레이어 조작
function getCurrentPlaying(self) {
    var target_id = $(self).data("target");
    var target_pk = $(self).data("pk");
    var audios = $(".audio-file");

    var player_current_time = $("#player-current-time");
    var player_play_btn = $("#player-play-btn");

    audios.each(function(index, item){
        if(!item.paused) {
            $(item).on("play", function() {
                playerDuration(item);
                $(item).on("loadedmetadata", function() {
                    playerDuration(item);
                })
            });

            playerCurrentTime(item);

            $(item).on("ended", function() {
                player_current_time.text("00:00");
                player_play_btn.find("[data-fa-processed]").removeClass("fa-pause");
                player_play_btn.find("[data-fa-processed]").addClass("fa-play");
            });

            player_play_btn.attr("data-target", target_id);
            player_play_btn.attr("data-pk", target_pk)
        }
        else {
            $(item).off()
        }
    });
}


// 플레이어 버튼 클릭시 조작
function playerPlayBtn(self) {
    if ($(self).attr("data-target") !== null) {
        var target_pk = $(self).attr("data-pk");
        playAudio(target_pk)
    }
}

// 플레이 리스트에 추가함
// play = true 인 경우 추가하고 바로 재생
function addToPlaylist(self) {
    var target_pk = $(self).data("src");
    var target_obj = $("#track-" + target_pk);
    var target_title = target_obj.data("title");
    var target_audio_id = target_obj.find("audio").attr("id");

    var ul = $("#player-playlist");
    var li = $(".player-playlist-item");
    var list_item = '<li class="player-playlist-item"><a data-target-pk="' + target_pk + '" onclick="playItem(this, event)" href="' + target_audio_id + '">' + target_title + '</a></li>';

    var exists_in_playlist = false;

    li.each(function(index, item) {
        if (item.outerHTML === list_item) {
            exists_in_playlist = item.outerHTML === list_item
        }
    });

    if (exists_in_playlist) {
    }
    else {
        ul.prepend(list_item);
    }
}

// 플레이리스트 내의 아이템 하나를 재생
function playItem(self, e) {
    e.preventDefault();
    var target_pk = $(self).attr("data-target-pk");
    var audio_pk = $(self).attr("href");
    var player_audio = $("#" + audio_pk);
    player_audio.on("loadedmetadata", playerDuration(player_audio[0], true));
    playAudio(target_pk);
    playerCurrentTime(player_audio[0])
}

function updatePlayerProgress(audio) {
    var progress_cover = $(".player-progress-cover");
    var current = audio.currentTime;
    var total = audio.duration;
    var position = current / total * 100;
    if ($(audio).attr("loaded")) {
        $(audio).on("timeupdate", function() {
            progress_cover.css("width", position + "%")
        });
    }
}

