# Notification Forwarding (iOS)

## What this does
This skill is for notifications the user forwards to Muse, not for reading the iPhone's system notification centre directly.

## Verified limitation (2026-10-23, iPhone, user 帅东)
- Muse iOS device commands (35 total) contain no notification-read command. Trying `notifications.list` returns `node_command_unsupported`.
- Device data sources are: calendar, contacts, health, location, reminders. No notifications source.
- Enabled permissions include `notifications_post` (Muse sending pushes to the user), not reading other apps' notifications.
- iOS does not offer a general "read other apps' notifications" permission to third-party apps in China. The new notification-forwarding in iOS 26.3 is for third-party accessories in the EU under the DMA, not for Muse in China.

## How to use it instead
1. When a notification matters, the user forwards it to Muse: share sheet, screenshot, or copy-paste the text.
2. Muse reads the forwarded content, extracts: app, time, sender, action required, deadline.
3. Muse acts only within the user's existing request for that notification (e.g. reply, add a reminder, check a calendar event). It does not send the content to anyone else unless the user asks.
4. For recurring checks, use a scheduled job against sources Muse already has (calendar, reminders), not against the notification centre.

## What not to claim
Do not claim Muse can read system notifications automatically, poll the notification centre, or that enabling a permission in iOS Settings will create such a channel. If the user asks for automatic reading, explain the limitation above and offer the forwarding route.
