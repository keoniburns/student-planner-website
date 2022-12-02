var calendar = new Calendar("calendarContainer",         // HTML container ID,                                                                     Required
    "large",                     // Size: (small, medium, large)                                                           Required
    ["Sunday", 3],               // [ Starting day, day abbreviation length ]                                              Required
    ["#ffc107",                 // Primary Color                                                                          Required
        "#ffa000",                 // Primary Dark Color                                                                     Required
        "#ffffff",                 // Text Color                                                                             Required
        "#ffecb3"],               // Text Dark Color                                                                        Required
    { // Following is optional
        days: ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
        months: ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
        indicator: true,         // Day Event Indicator                                                                    Optional
        indicator_type: 1,       // Day Event Indicator Type (0 not to display num of events, 1 to display num of events)  Optional
        indicator_pos: "bottom", // Day Event Indicator Position (top, bottom)                                             Optional
        placeholder: "<span>Custom Placeholder</span>"
    });

// Days Block click listener
calendar.setOnClickListener('days-blocks',
    // Called when a day block is clicked
    function () {
        console.log("Day block clicked");
    }
);

// Month Slider (Left and Right Arrow) Click Listeners
calendar.setOnClickListener('month-slider',
    // Called when the month left arrow is clicked
    function () {
        console.log("Month back slider clicked");
    },
    // Called when the month right arrow is clicked
    function () {
        console.log("Month next slider clicked");
    }
);

// Year Slider (Left and Right Arrow) Click Listeners
calendar.setOnClickListener('year-slider',
    // Called when the year left arrow is clicked
    function () {
        console.log("Year back slider clicked");
    },
    // Called when the year right arrow is clicked
    function () {
        console.log("Year next slider clicked");
    }
);



// var data = {
//     2022: {
//         12: {
//             25: [
//                 {
//                     startTime: "00:00",
//                     endTime: "24:00",
//                     text: "Christmas Day"
//                 }
//             ]
//         }
//     }
// };
// var organizer = new Organizer("organizerContainer", // Organizer container id                      Required
//     calendar,             // Calendar item                               Required
//     data);                // Events data (Must follow specified format)  Required
