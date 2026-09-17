# DB2ADMIN.SALESDOCUMENTIE

- **Module**: `SALES` (high confidence — table name starts with 'SALESDOCUMENT')
- **Roles**: `business_data`
- **Columns**: 20
- **Primary key**: `COMPANYCODE`, `PROVISIONALCOUNTERCODE`, `PROVISIONALCODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 143825

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `PROVISIONALCOUNTERCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 2 | `PROVISIONALCOUNTERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 3 | `PROVISIONALCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 4 | `TAXTEMPLATETEMPLATETYPE` | CHAR(2) |  |  |  |  |
| 5 | `TAXTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 6 | `FLAG` | CHAR(15) |  |  |  |  |
| 7 | `SAPMESSAGE` | LONG VARCHAR |  |  |  |  |
| 8 | `BASICVALUE` | DECIMAL(18,5) |  |  |  |  |
| 9 | `GROSSVALUE` | DECIMAL(18,5) |  |  |  |  |
| 10 | `ROUNDOFFVALUE` | DECIMAL(18,5) |  |  |  |  |
| 11 | `NETTVALUE` | DECIMAL(18,5) |  |  |  |  |
| 12 | `ROUNDOFFITAXCODE` | CHAR(3) |  |  |  |  |
| 13 | `FINDOCBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 14 | `FINDOCFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 15 | `FINDOCTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 16 | `FINDOCSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 17 | `FINDOCCODE` | CHAR(15) |  |  |  |  |
| 18 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 19 | `OTHFINDOCCODE` | CHAR(15) |  |  |  |  |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `SALESDOCUMENTIE.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SALESDOCUMENTIEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.PROVISIONALCOUNTERCOMPANYCODE,
       t.PROVISIONALCOUNTERCODE,
       t.PROVISIONALCODE,
       t.TAXTEMPLATETEMPLATETYPE,
       t.TAXTEMPLATECODE,
       t.FLAG,
       t.SAPMESSAGE,
       t.BASICVALUE,
       t.GROSSVALUE,
       t.ROUNDOFFVALUE,
       t.NETTVALUE
FROM   DB2ADMIN.SALESDOCUMENTIE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
