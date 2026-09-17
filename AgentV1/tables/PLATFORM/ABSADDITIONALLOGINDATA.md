# DB2ADMIN.ABSADDITIONALLOGINDATA

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 11
- **Primary key**: `CODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 162

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CODE` | CHAR(65) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 1 | `DESCRIPTION` | LONG VARCHAR |  |  | description |  |
| 2 | `IMAGEPATH` | VARCHAR(1000) |  |  |  |  |
| 3 | `IMAGENAME` | VARCHAR(250) | NOT NULL |  |  |  |
| 4 | `DEFAULTVALUE` | CHAR(50) |  |  |  |  |
| 5 | `SEQUENCE` | INTEGER | NOT NULL |  |  |  |
| 6 | `REFERENCEUIPATH` | VARCHAR(50) |  |  |  |  |
| 7 | `REFERENCEUINAME` | VARCHAR(54) |  |  |  |  |
| 8 | `OTHERKEYSUI` | VARCHAR(100) |  |  |  |  |
| 9 | `LABELUI` | CHAR(50) |  |  |  |  |
| 10 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ABSADDITIONALLOGINDATAUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CODE,
       t.DESCRIPTION,
       t.IMAGEPATH,
       t.IMAGENAME,
       t.DEFAULTVALUE,
       t.SEQUENCE,
       t.REFERENCEUIPATH,
       t.REFERENCEUINAME,
       t.OTHERKEYSUI,
       t.LABELUI,
       t.ABSUNIQUEID
FROM   DB2ADMIN.ABSADDITIONALLOGINDATA t
FETCH FIRST 100 ROWS ONLY;
```
