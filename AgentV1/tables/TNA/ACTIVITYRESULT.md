# DB2ADMIN.ACTIVITYRESULT

- **Module**: `TNA` (low confidence — FK neighbourhood: 1 of 1 related tables are TNA)
- **Roles**: `business_data`
- **Columns**: 13
- **Primary key**: `ACTIVITYRESULTTYPECOMPANYCODE`, `ACTIVITYRESULTTYPECODE`, `CODE`
- **FK degree**: referenced by 1 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 191137

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ACTIVITYRESULTTYPECOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `ACTIVITYRESULTTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `CODE` | CHAR(10) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 4 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 5 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 6 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 7 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 8 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 9 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 10 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 11 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 12 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ACTIVITYRESULTTYPE_RESULTS` | `ACTIVITYRESULTTYPECOMPANYCODE`, `ACTIVITYRESULTTYPECODE` | [`ACTIVITYRESULTTYPE`](../TNA/ACTIVITYRESULTTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ACTIVITYRESULT.ACTIVITYRESULTTYPECOMPANYCODE = ACTIVITYRESULTTYPE.COMPANYCODE AND ACTIVITYRESULT.ACTIVITYRESULTTYPECODE = ACTIVITYRESULTTYPE.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `ACTIVITYRESULT_RESULTCODE` | [`NEXTACTIVITIES`](../TNA/NEXTACTIVITIES.md) | `TNADETAILTNAHEADERCOMPANYCODE`, `CODE`, `RESULTCODECODE` | `NEXTACTIVITIES.TNADETAILTNAHEADERCOMPANYCODE = ACTIVITYRESULT.ACTIVITYRESULTTYPECOMPANYCODE AND NEXTACTIVITIES.CODE = ACTIVITYRESULT.ACTIVITYRESULTTYPECODE AND NEXTACTIVITIES.RESULTCODECODE = ACTIVITYRESULT.CODE` |

## Indexes

- `ACTIVITYRESULTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ACTIVITYRESULTTYPECOMPANYCODE,
       t.ACTIVITYRESULTTYPECODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC
FROM   DB2ADMIN.ACTIVITYRESULT t
FETCH FIRST 100 ROWS ONLY;
```
