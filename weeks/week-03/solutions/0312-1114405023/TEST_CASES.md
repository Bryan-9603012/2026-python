# TEST_CASES

## Case 1：左轉測試
- 輸入：
  - 初始方向：N
  - 指令：L
- 預期結果：
  - 方向變成 W
- 實際結果：
  - W
- 狀態：
  - PASS
- 對應測試：
  - `test_turn_left_from_north`

---

## Case 2：右轉測試
- 輸入：
  - 初始方向：N
  - 指令：R
- 預期結果：
  - 方向變成 E
- 實際結果：
  - E
- 狀態：
  - PASS
- 對應測試：
  - `test_turn_right_from_north`

---

## Case 3：四次左轉回原方向
- 輸入：
  - 初始方向：N
  - 指令：LLLL
- 預期結果：
  - 最後方向仍為 N
- 實際結果：
  - N
- 狀態：
  - PASS
- 對應測試：
  - `test_turn_left_four_times_back_to_original`

---

## Case 4：四次右轉回原方向
- 輸入：
  - 初始方向：N
  - 指令：RRRR
- 預期結果：
  - 最後方向仍為 N
- 實際結果：
  - N
- 狀態：
  - PASS
- 對應測試：
  - `test_turn_right_four_times_back_to_original`

---

## Case 5：機器人正常前進
- 輸入：
  - 初始狀態：Robot(1, 1, 'N')
  - 指令：F
  - 地圖：5 x 3
- 預期結果：
  - 新位置為 (1, 2)
  - 未 LOST
- 實際結果：
  - (1, 2), LOST=False
- 狀態：
  - PASS
- 對應測試：
  - `test_robot_moves_forward_inside_grid`

---

## Case 6：機器人越界變 LOST
- 輸入：
  - 初始狀態：Robot(3, 3, 'N')
  - 指令：F
  - 地圖：5 x 3
- 預期結果：
  - 機器人 LOST
  - scent 新增 (3, 3, 'N')
- 實際結果：
  - LOST=True
  - scent = {(3, 3, 'N')}
- 狀態：
  - PASS
- 對應測試：
  - `test_robot_becomes_lost_when_moving_out_of_bounds`

---

## Case 7：有 scent 時忽略危險前進
- 輸入：
  - 初始狀態：Robot(3, 3, 'N')
  - 指令：F
  - 地圖：5 x 3
  - scents = {(3, 3, 'N')}
- 預期結果：
  - 機器人不移動
  - 不 LOST
- 實際結果：
  - (3, 3, 'N'), LOST=False
- 狀態：
  - PASS
- 對應測試：
  - `test_second_robot_ignores_scented_danger`

---

## Case 8：同位置不同方向不共用 scent
- 輸入：
  - 初始狀態：Robot(3, 3, 'E')
  - 指令：F
  - 地圖：3 x 3
  - scents = {(3, 3, 'N')}
- 預期結果：
  - 因方向不同，不受原 scent 保護
  - 機器人 LOST
- 實際結果：
  - LOST=True
- 狀態：
  - PASS
- 對應測試：
  - `test_same_position_different_direction_not_protected_by_scent`

---

## Case 9：LOST 後停止後續指令
- 輸入：
  - 初始狀態：Robot(3, 3, 'N')
  - 指令：FRF
  - 地圖：5 x 3
- 預期結果：
  - 第一個 F 後 LOST
  - 後面指令不再執行
- 實際結果：
  - (3, 3, 'N'), LOST=True
- 狀態：
  - PASS
- 對應測試：
  - `test_robot_stops_after_lost`

---

## Case 10：非法指令拋出錯誤
- 輸入：
  - 初始狀態：Robot(1, 1, 'N')
  - 指令：X
- 預期結果：
  - 拋出 `ValueError`
- 實際結果：
  - 成功拋出 `ValueError`
- 狀態：
  - PASS
- 對應測試：
  - `test_invalid_command_raises_value_error`