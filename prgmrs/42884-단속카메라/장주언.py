def solution(routes):
    lst = routes
    lst.sort(key=lambda x: x[1])



    cam = []

    cam.append(lst[0][1])

    for idx in range(1, len(routes)):

      start, end = lst[idx]
      if start > cam[-1]:
          cam.append(end)

    answer = len(cam)

    return answer

# def solution(routes):
#
#     routes.sort(key=lambda info: info[1])
#
#     last_camera = routes[0][1]
#
#     answer = 1
#
#     for idx in range(1, len(routes)):
#         start, end = routes[idx]
#         if start > last_camera:
#             last_camera = end
#             answer += 1
#     return answer







# 2
print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]]))