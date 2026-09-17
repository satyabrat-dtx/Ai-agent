# DB2ADMIN.FLATBANK

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 26
- **Primary key**: `DIVISIONCODE`, `COMPANYCODE`, `UPLOADID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 103980

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK | primary_key | Division within a company; second-level organisational discriminator. |
| 1 | `COMPANYCODE` | CHAR(8) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `UPLOADID` | DECIMAL(9,0) | NOT NULL | PK | primary_key |  |
| 3 | `FIRMENGRUPPE` | CHAR(8) |  |  |  |  |
| 4 | `BIC` | CHAR(11) |  |  |  |  |
| 5 | `HAUSBANK` | CHAR(20) |  |  |  |  |
| 6 | `HAUSBANKBEZ` | VARCHAR(140) |  |  |  |  |
| 7 | `HAUSBANKBEZ2` | VARCHAR(140) |  |  |  |  |
| 8 | `HAUSBANKORT` | CHAR(50) |  |  |  |  |
| 9 | `IBAN` | CHAR(34) |  |  |  |  |
| 10 | `KREDITLIMIT` | DECIMAL(17,2) |  |  |  |  |
| 11 | `KREDITLIMITLW` | DECIMAL(17,2) |  |  |  |  |
| 12 | `SACHKONTO` | CHAR(10) |  |  |  |  |
| 13 | `SACHKONTOBEZ` | VARCHAR(140) |  |  |  |  |
| 14 | `SACHKONTOBEZ2` | VARCHAR(140) |  |  |  |  |
| 15 | `SALDO` | DECIMAL(17,2) |  |  |  |  |
| 16 | `SALDOLW` | DECIMAL(17,2) |  |  |  |  |
| 17 | `ZMUSALDO` | DECIMAL(17,2) |  |  |  |  |
| 18 | `ZMUSALDOLW` | DECIMAL(17,2) |  |  |  |  |
| 19 | `ZMUKONTO` | CHAR(10) |  |  |  |  |
| 20 | `ZMUKONTOBEZ` | VARCHAR(140) |  |  |  |  |
| 21 | `WAEHRUNG` | CHAR(3) |  |  |  |  |
| 22 | `ZMUKONTOBEZ2` | VARCHAR(140) |  |  |  |  |
| 23 | `SH` | CHAR(1) |  |  |  |  |
| 24 | `SALDODATUM` | DATE |  |  |  |  |
| 25 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FLATBANKUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.DIVISIONCODE,
       t.COMPANYCODE,
       t.UPLOADID,
       t.FIRMENGRUPPE,
       t.BIC,
       t.HAUSBANK,
       t.HAUSBANKBEZ,
       t.HAUSBANKBEZ2,
       t.HAUSBANKORT,
       t.IBAN,
       t.KREDITLIMIT,
       t.KREDITLIMITLW
FROM   DB2ADMIN.FLATBANK t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
