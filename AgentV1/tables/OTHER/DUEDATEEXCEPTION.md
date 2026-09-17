# DB2ADMIN.DUEDATEEXCEPTION

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 27
- **Primary key**: `CODE`
- **FK degree**: referenced by 3 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 194457

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CODE` | CHAR(6) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 1 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 2 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 3 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 4 | `STARTDATE1` | CHAR(4) |  |  |  |  |
| 5 | `STARTDATE2` | CHAR(4) |  |  |  |  |
| 6 | `STARTDATE3` | CHAR(4) |  |  |  |  |
| 7 | `STARTDATE4` | CHAR(4) |  |  |  |  |
| 8 | `STARTDATE5` | CHAR(4) |  |  |  |  |
| 9 | `ENDDATE1` | CHAR(4) |  |  |  |  |
| 10 | `ENDDATE2` | CHAR(4) |  |  |  |  |
| 11 | `ENDDATE3` | CHAR(4) |  |  |  |  |
| 12 | `ENDDATE4` | CHAR(4) |  |  |  |  |
| 13 | `ENDDATE5` | CHAR(4) |  |  |  |  |
| 14 | `POSTPONEDATE1` | CHAR(4) |  |  |  |  |
| 15 | `POSTPONEDATE2` | CHAR(4) |  |  |  |  |
| 16 | `POSTPONEDATE3` | CHAR(4) |  |  |  |  |
| 17 | `POSTPONEDATE4` | CHAR(4) |  |  |  |  |
| 18 | `POSTPONEDATE5` | CHAR(4) |  |  |  |  |
| 19 | `NOTE` | VARCHAR(140) |  |  |  |  |
| 20 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 21 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 22 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 23 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 24 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 25 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 26 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 3

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `DUEDATEEXCEPTION_DUEDATEEXCEPTION` | [`PAYMENTMETHOD`](../CORE_MASTER/PAYMENTMETHOD.md) | `DUEDATEEXCEPTIONCODE` | `PAYMENTMETHOD.DUEDATEEXCEPTIONCODE = DUEDATEEXCEPTION.CODE` |
| `DUEDATEEXCEPTION_DUEDATEEXCEPTION` | [`ORDERPARTNER`](../CORE_MASTER/ORDERPARTNER.md) | `DUEDATEEXCEPTIONCODE` | `ORDERPARTNER.DUEDATEEXCEPTIONCODE = DUEDATEEXCEPTION.CODE` |
| `DUEDATEEXCEPTION_DUEDATEEXCEPTION` | [`ORDERPARTNERSPECIALIZEDDATA`](../OTHER/ORDERPARTNERSPECIALIZEDDATA.md) | `DUEDATEEXCEPTIONCODE` | `ORDERPARTNERSPECIALIZEDDATA.DUEDATEEXCEPTIONCODE = DUEDATEEXCEPTION.CODE` |

## Indexes

- `DUEDATEEXCEPTIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.STARTDATE1,
       t.STARTDATE2,
       t.STARTDATE3,
       t.STARTDATE4,
       t.STARTDATE5,
       t.ENDDATE1,
       t.ENDDATE2,
       t.ENDDATE3
FROM   DB2ADMIN.DUEDATEEXCEPTION t
FETCH FIRST 100 ROWS ONLY;
```
