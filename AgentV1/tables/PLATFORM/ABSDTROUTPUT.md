# DB2ADMIN.ABSDTROUTPUT

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 15
- **Primary key**: `ABSDTRENTITYGROUPFAMILY`, `ABSDTRENTITYREFERENCEDENTITY`, `ABSDTRENTITYDTRPKTOKEN`, `FIELDNAME`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 96736

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ABSDTRENTITYGROUPFAMILY` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `ABSDTRENTITYREFERENCEDENTITY` | CHAR(50) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `OUTPUTSEQUENCE` | INTEGER | NOT NULL |  |  |  |
| 3 | `FIELDNAME` | VARCHAR(120) | NOT NULL | PK | primary_key |  |
| 4 | `DATATYPE` | INTEGER | NOT NULL |  |  |  |
| 5 | `OUTPUTMANDATORY` | SMALLINT | NOT NULL |  |  |  |
| 6 | `FIELDLABEL` | CHAR(30) | NOT NULL |  |  |  |
| 7 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 8 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 9 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 10 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 11 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 12 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 13 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 14 | `ABSDTRENTITYDTRPKTOKEN` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ABSDTRENTITY_DTROUTPUT` | `ABSDTRENTITYGROUPFAMILY`, `ABSDTRENTITYREFERENCEDENTITY`, `ABSDTRENTITYDTRPKTOKEN` | [`ABSDTRENTITY`](../PLATFORM/ABSDTRENTITY.md) | `GROUPFAMILY`, `REFERENCEDENTITY`, `DTRPKTOKEN` | RESTRICT | `ABSDTROUTPUT.ABSDTRENTITYGROUPFAMILY = ABSDTRENTITY.GROUPFAMILY AND ABSDTROUTPUT.ABSDTRENTITYREFERENCEDENTITY = ABSDTRENTITY.REFERENCEDENTITY AND ABSDTROUTPUT.ABSDTRENTITYDTRPKTOKEN = ABSDTRENTITY.DTRPKTOKEN` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ABSDTROUTPUTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ABSDTRENTITYGROUPFAMILY,
       t.ABSDTRENTITYREFERENCEDENTITY,
       t.OUTPUTSEQUENCE,
       t.FIELDNAME,
       t.DATATYPE,
       t.OUTPUTMANDATORY,
       t.FIELDLABEL,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.ABSUNIQUEID
FROM   DB2ADMIN.ABSDTROUTPUT t
FETCH FIRST 100 ROWS ONLY;
```
