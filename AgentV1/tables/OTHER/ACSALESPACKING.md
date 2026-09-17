# DB2ADMIN.ACSALESPACKING

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 13
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 42225

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(15) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `COMMENTS` | CHAR(50) |  |  |  |  |
| 3 | `NETWEIGHT` | DECIMAL(15,5) |  |  |  |  |
| 4 | `GROSSWEIGHT` | DECIMAL(15,5) |  |  |  |  |
| 5 | `HEIGHT` | DECIMAL(15,5) |  |  |  |  |
| 6 | `WIDTH` | DECIMAL(15,5) |  |  |  |  |
| 7 | `LENGTH` | DECIMAL(15,5) |  |  |  |  |
| 8 | `VOLUME` | DECIMAL(15,5) |  |  |  |  |
| 9 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 10 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 11 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 12 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.COMMENTS,
       t.NETWEIGHT,
       t.GROSSWEIGHT,
       t.HEIGHT,
       t.WIDTH,
       t.LENGTH,
       t.VOLUME,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME
FROM   DB2ADMIN.ACSALESPACKING t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
