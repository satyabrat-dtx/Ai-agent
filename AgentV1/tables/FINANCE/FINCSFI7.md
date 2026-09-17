# DB2ADMIN.FINCSFI7

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 14
- **Primary key**: `COMPANYCODE`, `DIVISIONCODE`, `URSVIDA`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 103819

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(8) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(8) | NOT NULL | PK | primary_key | Division within a company; second-level organisational discriminator. |
| 2 | `URSVIDA` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 3 | `URSVID` | CHAR(12) |  |  |  |  |
| 4 | `URSVREPREPID` | CHAR(3) |  | FK | foreign_key |  |
| 5 | `URSVNAME` | CHAR(50) |  |  |  |  |
| 6 | `URSVTXT` | VARCHAR(255) |  |  |  |  |
| 7 | `URSVNAME2` | CHAR(50) |  |  |  |  |
| 8 | `URSVTXT2` | VARCHAR(255) |  |  |  |  |
| 9 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 10 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 11 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 12 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 13 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `FINCSFI1_URSVREP` | `URSVREPREPID` | [`FINCSFI1`](../FINANCE/FINCSFI1.md) | `REPID` | RESTRICT | `FINCSFI7.URSVREPREPID = FINCSFI1.REPID` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FINCSFI7UID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.URSVIDA,
       t.URSVID,
       t.URSVREPREPID,
       t.URSVNAME,
       t.URSVTXT,
       t.URSVNAME2,
       t.URSVTXT2,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME
FROM   DB2ADMIN.FINCSFI7 t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
