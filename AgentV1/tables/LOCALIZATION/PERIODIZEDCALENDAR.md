# DB2ADMIN.PERIODIZEDCALENDAR

- **Module**: `LOCALIZATION` (low confidence — FK neighbourhood: 1 of 1 related tables are LOCALIZATION)
- **Roles**: `business_data`
- **Columns**: 12
- **Primary key**: `TYPECODE`, `YEAR`
- **FK degree**: referenced by 3 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 18441

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `TYPECODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `YEAR` | DECIMAL(4,0) | NOT NULL | PK | primary_key |  |
| 2 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 3 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 4 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 5 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 6 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 7 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 8 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 9 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 10 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 11 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `PERIODIZEDCALENDARTYPE_TYPE` | `TYPECODE` | [`PERIODIZEDCALENDARTYPE`](../CORE_MASTER/PERIODIZEDCALENDARTYPE.md) | `CODE` | RESTRICT | `PERIODIZEDCALENDAR.TYPECODE = PERIODIZEDCALENDARTYPE.CODE` |

## Referenced by (child → this table) — 3

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `PERIODIZEDCALENDAR_PERIOD` | [`PERIOD`](../WAREHOUSE/PERIOD.md) | `PERIODIZEDCALENDARTYPECODE`, `PERIODIZEDCALENDARYEAR` | `PERIOD.PERIODIZEDCALENDARTYPECODE = PERIODIZEDCALENDAR.TYPECODE AND PERIOD.PERIODIZEDCALENDARYEAR = PERIODIZEDCALENDAR.YEAR` |
| `PERIODIZEDCALENDAR_PERIODIZEDCALENDAR` | [`STATISTICALGROUP`](../CORE_MASTER/STATISTICALGROUP.md) | `PERIODIZEDCALENDARTYPECODE`, `PERIODIZEDCALENDARYEAR` | `STATISTICALGROUP.PERIODIZEDCALENDARTYPECODE = PERIODIZEDCALENDAR.TYPECODE AND STATISTICALGROUP.PERIODIZEDCALENDARYEAR = PERIODIZEDCALENDAR.YEAR` |
| `PERIODIZEDCALENDAR_WIPPERIODIZEDCALENDAR` | [`USACUSTOMIZEDOPTIONS`](../LOCALIZATION/USACUSTOMIZEDOPTIONS.md) | `WIPPERIODIZEDCALENDARTYPECODE`, `WIPPERIODIZEDCALENDARYEAR` | `USACUSTOMIZEDOPTIONS.WIPPERIODIZEDCALENDARTYPECODE = PERIODIZEDCALENDAR.TYPECODE AND USACUSTOMIZEDOPTIONS.WIPPERIODIZEDCALENDARYEAR = PERIODIZEDCALENDAR.YEAR` |

## Indexes

- `PERIODIZEDCALENDARUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.TYPECODE,
       t.YEAR,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.ABSUNIQUEID,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC
FROM   DB2ADMIN.PERIODIZEDCALENDAR t
FETCH FIRST 100 ROWS ONLY;
```
