# DB2ADMIN.ACTIVITY

- **Module**: `TNA` (low confidence — FK neighbourhood: 2 of 3 related tables are TNA)
- **Roles**: `business_data`
- **Columns**: 23
- **Primary key**: `CODE`
- **FK degree**: referenced by 6 constraint(s), references 5 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 118272

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `TYPE` | INTEGER | NOT NULL |  |  |  |
| 1 | `CODE` | CHAR(15) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 3 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 4 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 5 | `ACTIVITYGROUPCODE` | CHAR(10) |  | FK | foreign_key |  |
| 6 | `DURATIONREQD` | INTEGER | NOT NULL |  |  |  |
| 7 | `DURATIONUM` | INTEGER | NOT NULL |  |  |  |
| 8 | `USERRESPNSBLUSERID` | CHAR(50) |  | FK | foreign_key |  |
| 9 | `MESSAGETYPE` | INTEGER | NOT NULL |  |  |  |
| 10 | `MESSAGETOUSERID` | CHAR(50) |  | FK | foreign_key |  |
| 11 | `MESSAGEWHEN` | CHAR(90) |  |  |  |  |
| 12 | `ESCALATIONDURATIONREQD` | INTEGER | NOT NULL |  |  |  |
| 13 | `ESCALATIONDURATIONUM` | INTEGER | NOT NULL |  |  |  |
| 14 | `ESCALATIONUSERRESPNSBLUSERID` | CHAR(50) |  | FK | foreign_key |  |
| 15 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 16 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 17 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 18 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 19 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 20 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 21 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 22 | `TASKMANAGERUSERID` | CHAR(50) |  | FK | foreign_key |  |

## References (this table → parent) — 5

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ABSUSERDEF_ESCALATIONUSERRESPNSBL` | `ESCALATIONUSERRESPNSBLUSERID` | [`ABSUSERDEF`](../PLATFORM/ABSUSERDEF.md) | `USERID` | RESTRICT | `ACTIVITY.ESCALATIONUSERRESPNSBLUSERID = ABSUSERDEF.USERID` |
| `ABSUSERDEF_MESSAGETO` | `MESSAGETOUSERID` | [`ABSUSERDEF`](../PLATFORM/ABSUSERDEF.md) | `USERID` | RESTRICT | `ACTIVITY.MESSAGETOUSERID = ABSUSERDEF.USERID` |
| `ABSUSERDEF_TASKMANAGER` | `TASKMANAGERUSERID` | [`ABSUSERDEF`](../PLATFORM/ABSUSERDEF.md) | `USERID` | RESTRICT | `ACTIVITY.TASKMANAGERUSERID = ABSUSERDEF.USERID` |
| `ABSUSERDEF_USERRESPNSBL` | `USERRESPNSBLUSERID` | [`ABSUSERDEF`](../PLATFORM/ABSUSERDEF.md) | `USERID` | RESTRICT | `ACTIVITY.USERRESPNSBLUSERID = ABSUSERDEF.USERID` |
| `ACTIVITYGROUP_ACTIVITYGROUP` | `ACTIVITYGROUPCODE` | [`ACTIVITYGROUP`](../TNA/ACTIVITYGROUP.md) | `CODE` | RESTRICT | `ACTIVITY.ACTIVITYGROUPCODE = ACTIVITYGROUP.CODE` |

## Referenced by (child → this table) — 6

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `ACTIVITY_ACTIVITY` | [`CSRMACTIVITYDETAIL`](../PLATFORM/CSRMACTIVITYDETAIL.md) | `ACTIVITYCODE` | `CSRMACTIVITYDETAIL.ACTIVITYCODE = ACTIVITY.CODE` |
| `ACTIVITY_ACTIVITYBASEDON` | [`CSRMACTIVITYDETAIL`](../PLATFORM/CSRMACTIVITYDETAIL.md) | `ACTIVITYBASEDONCODE` | `CSRMACTIVITYDETAIL.ACTIVITYBASEDONCODE = ACTIVITY.CODE` |
| `ACTIVITY_ACTIVITYBASEDON` | [`TNAACTIVITYDETAIL`](../TNA/TNAACTIVITYDETAIL.md) | `ACTIVITYBASEDONCODE` | `TNAACTIVITYDETAIL.ACTIVITYBASEDONCODE = ACTIVITY.CODE` |
| `ACTIVITY_ACTIVITYCODE` | [`TNAACTIVITYDETAIL`](../TNA/TNAACTIVITYDETAIL.md) | `ACTIVITYCODECODE` | `TNAACTIVITYDETAIL.ACTIVITYCODECODE = ACTIVITY.CODE` |
| `ACTIVITY_ACTIVITYBASEDON` | [`TNADETAIL`](../TNA/TNADETAIL.md) | `ACTIVITYBASEDONCODE` | `TNADETAIL.ACTIVITYBASEDONCODE = ACTIVITY.CODE` |
| `ACTIVITY_ACTIVITYCODE` | [`TNADETAIL`](../TNA/TNADETAIL.md) | `ACTIVITYCODECODE` | `TNADETAIL.ACTIVITYCODECODE = ACTIVITY.CODE` |

## Indexes

- `ACTIVITYUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.TYPE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.ACTIVITYGROUPCODE,
       t.DURATIONREQD,
       t.DURATIONUM,
       t.USERRESPNSBLUSERID,
       t.MESSAGETYPE,
       t.MESSAGETOUSERID,
       t.MESSAGEWHEN
FROM   DB2ADMIN.ACTIVITY t
FETCH FIRST 100 ROWS ONLY;
```
