# DB2ADMIN.FINEXPNEGOTIATIONPC

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 15
- **Primary key**: `COMPANYCODE`, `NEGOTIATIONCODE`, `PACKINGCREDITLETTERNO`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 176880

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `NEGOTIATIONCODE` | CHAR(5) | NOT NULL | PK | primary_key |  |
| 2 | `BANKREFERENCENO` | CHAR(30) |  |  |  |  |
| 3 | `REFERENCEDATE` | DATE |  |  |  |  |
| 4 | `PACKINGCREDITLETTERNO` | CHAR(5) | NOT NULL | PK | primary_key |  |
| 5 | `BUSINESSUNITCODE` | CHAR(10) |  | FK | foreign_key |  |
| 6 | `PACKINGCREDITVALUE` | DECIMAL(18,5) |  |  |  |  |
| 7 | `PACKINGCREDITBALANCEVALUE` | DECIMAL(18,5) |  |  |  |  |
| 8 | `ADJUSTFORTHISBILL` | DECIMAL(18,5) |  |  |  |  |
| 9 | `ADJUSTFCVALUE` | DECIMAL(18,5) |  |  |  |  |
| 10 | `BANKCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 11 | `BANKCODE` | CHAR(20) |  | FK | foreign_key |  |
| 12 | `REMARKS` | CHAR(100) |  |  |  |  |
| 13 | `EXCHANGERATE` | DECIMAL(6,3) |  |  |  |  |
| 14 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `FINBUSINESSUNIT_BUSINESSUNIT` | `COMPANYCODE`, `BUSINESSUNITCODE` | [`FINBUSINESSUNIT`](../FINANCE/FINBUSINESSUNIT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FINEXPNEGOTIATIONPC.COMPANYCODE = FINBUSINESSUNIT.COMPANYCODE AND FINEXPNEGOTIATIONPC.BUSINESSUNITCODE = FINBUSINESSUNIT.CODE` |
| `GLMASTER_BANK` | `BANKCOMPANYCODE`, `BANKCODE` | [`GLMASTER`](../CORE_MASTER/GLMASTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FINEXPNEGOTIATIONPC.BANKCOMPANYCODE = GLMASTER.COMPANYCODE AND FINEXPNEGOTIATIONPC.BANKCODE = GLMASTER.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FINEXPNEGOTIATIONPCUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.NEGOTIATIONCODE,
       t.BANKREFERENCENO,
       t.REFERENCEDATE,
       t.PACKINGCREDITLETTERNO,
       t.BUSINESSUNITCODE,
       t.PACKINGCREDITVALUE,
       t.PACKINGCREDITBALANCEVALUE,
       t.ADJUSTFORTHISBILL,
       t.ADJUSTFCVALUE,
       t.BANKCOMPANYCODE,
       t.BANKCODE
FROM   DB2ADMIN.FINEXPNEGOTIATIONPC t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
