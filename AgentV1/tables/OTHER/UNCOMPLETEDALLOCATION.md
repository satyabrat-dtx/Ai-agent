# DB2ADMIN.UNCOMPLETEDALLOCATION

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 7
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 11515

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(15) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `ALLOCATIONDATE` | DATE | NOT NULL |  |  |  |
| 3 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 4 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 5 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 6 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `UNCOMPLETEDALLOCATION.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.ALLOCATIONDATE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER
FROM   DB2ADMIN.UNCOMPLETEDALLOCATION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
