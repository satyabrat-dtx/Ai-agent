# DB2ADMIN.APPAGTORDPRNDELIVERYPOINT

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 12
- **Primary key**: `COMPANYCODE`, `AGENTCODE`, `ORDPRNCUSTOMERSUPPLIERTYPE`, `ORDPRNCUSTOMERSUPPLIERCODE`, `DELIVERYPOINTUNIQUEID`, `DELIVERYPOINTCODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 110578

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `AGENTCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `ORDPRNCUSTOMERSUPPLIERTYPE` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 3 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 4 | `DELIVERYPOINTUNIQUEID` | BIGINT | NOT NULL | PK | primary_key |  |
| 5 | `DELIVERYPOINTCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 6 | `NAME` | VARCHAR(100) |  |  |  |  |
| 7 | `ADDRESS` | VARCHAR(700) |  |  |  |  |
| 8 | `TOWN` | VARCHAR(100) |  |  |  |  |
| 9 | `PHONE` | VARCHAR(40) |  |  |  |  |
| 10 | `MAIL` | VARCHAR(100) |  |  |  |  |
| 11 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `APPAGTORDPRNDELIVERYPOINTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.AGENTCODE,
       t.ORDPRNCUSTOMERSUPPLIERTYPE,
       t.ORDPRNCUSTOMERSUPPLIERCODE,
       t.DELIVERYPOINTUNIQUEID,
       t.DELIVERYPOINTCODE,
       t.NAME,
       t.ADDRESS,
       t.TOWN,
       t.PHONE,
       t.MAIL,
       t.ABSUNIQUEID
FROM   DB2ADMIN.APPAGTORDPRNDELIVERYPOINT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
