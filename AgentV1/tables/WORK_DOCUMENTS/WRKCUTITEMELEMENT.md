# DB2ADMIN.WRKCUTITEMELEMENT

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 15
- **Primary key**: `COMPANYCODE`, `CREATIONTIMESTAMP`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 128166

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 2 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 4 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 5 | `ORIGINALELEMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 6 | `ORIGINALELEMENTSUBCODEKEY` | CHAR(20) |  |  |  |  |
| 7 | `ORIGINALELEMENTCODE` | CHAR(15) |  |  |  |  |
| 8 | `ORIGINALELEMENTQTY` | DECIMAL(15,5) |  |  |  |  |
| 9 | `ORIGINALELEMENTUOMCODE` | CHAR(3) |  |  |  |  |
| 10 | `CUTITEMELEMENTCODE` | CHAR(15) |  |  |  |  |
| 11 | `CUTITEMELEMENTQTY` | DECIMAL(15,5) |  |  |  |  |
| 12 | `PROJECTCODE` | CHAR(20) |  |  |  |  |
| 13 | `CUTSTATUS` | CHAR(10) |  |  |  |  |
| 14 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKCUTITEMELEMENTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CREATIONTIMESTAMP,
       t.LINENO,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.ORIGINALELEMENTCOMPANYCODE,
       t.ORIGINALELEMENTSUBCODEKEY,
       t.ORIGINALELEMENTCODE,
       t.ORIGINALELEMENTQTY,
       t.ORIGINALELEMENTUOMCODE,
       t.CUTITEMELEMENTCODE,
       t.CUTITEMELEMENTQTY
FROM   DB2ADMIN.WRKCUTITEMELEMENT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
