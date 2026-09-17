# DB2ADMIN.ABSDTRCONDITION

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 19
- **Primary key**: `ABSDTRENTITYGROUPFAMILY`, `ABSDTRENTITYREFERENCEDENTITY`, `ABSDTRENTITYDTRPKTOKEN`, `UNIQUEIDENT`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 96630

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ABSDTRENTITYGROUPFAMILY` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `ABSDTRENTITYREFERENCEDENTITY` | CHAR(50) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `UNIQUEIDENT` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `FIELDTYPE` | INTEGER | NOT NULL |  |  |  |
| 4 | `FIELDNAME` | VARCHAR(120) | NOT NULL |  |  |  |
| 5 | `CONDITIONSEQUENCE` | INTEGER | NOT NULL |  |  |  |
| 6 | `FIELDOPERATOR` | CHAR(9) | NOT NULL |  |  |  |
| 7 | `PLYENABLED` | SMALLINT | NOT NULL |  |  |  |
| 8 | `CONDITIONMANDATORY` | SMALLINT | NOT NULL |  |  |  |
| 9 | `FIELDLABEL` | CHAR(30) |  |  |  |  |
| 10 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 11 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 12 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 13 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 14 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 15 | `JAVANAME` | VARCHAR(100) |  |  |  |  |
| 16 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 17 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 18 | `ABSDTRENTITYDTRPKTOKEN` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ABSDTRENTITY_DTRINPUT` | `ABSDTRENTITYGROUPFAMILY`, `ABSDTRENTITYREFERENCEDENTITY`, `ABSDTRENTITYDTRPKTOKEN` | [`ABSDTRENTITY`](../PLATFORM/ABSDTRENTITY.md) | `GROUPFAMILY`, `REFERENCEDENTITY`, `DTRPKTOKEN` | RESTRICT | `ABSDTRCONDITION.ABSDTRENTITYGROUPFAMILY = ABSDTRENTITY.GROUPFAMILY AND ABSDTRCONDITION.ABSDTRENTITYREFERENCEDENTITY = ABSDTRENTITY.REFERENCEDENTITY AND ABSDTRCONDITION.ABSDTRENTITYDTRPKTOKEN = ABSDTRENTITY.DTRPKTOKEN` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ABSDTRCONDITIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ABSDTRENTITYGROUPFAMILY,
       t.ABSDTRENTITYREFERENCEDENTITY,
       t.UNIQUEIDENT,
       t.FIELDTYPE,
       t.FIELDNAME,
       t.CONDITIONSEQUENCE,
       t.FIELDOPERATOR,
       t.PLYENABLED,
       t.CONDITIONMANDATORY,
       t.FIELDLABEL,
       t.CREATIONDATETIME,
       t.CREATIONUSER
FROM   DB2ADMIN.ABSDTRCONDITION t
FETCH FIRST 100 ROWS ONLY;
```
