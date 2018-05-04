$(document).ready(function() {
		$('#calendar').fullCalendar({
			header: {
				left: 'prev,next today',
				center: 'title',
				right: 'month,agendaWeek'
			},
            defaultDate: $('#calendar').fullCalendar('today'),
            nowIndicator: true,
			editable: true,
			eventLimit: true, // allow "more" link when too many events
			events: {
				url: 'data',
				error: function() {
					$('#script-warning').show();
				}
			},
			loading: function(bool) {
				$('#loading').toggle(bool);
			}
		});
	});
