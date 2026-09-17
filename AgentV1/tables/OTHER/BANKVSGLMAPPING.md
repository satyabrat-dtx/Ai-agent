# DB2ADMIN.BANKVSGLMAPPING

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `COMPANYCODE`, `BANKIDIDENTIFIER`, `BANKBANKCOUNTRYCODE`, `BANKCODE`, `BANKBRANCHCODE`, `ACCOUNTID`, `FROMDATE`
- **FK degree**: referenced by 0 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 221216

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `BANKIDIDENTIFIER` | DECIMAL(3,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `BANKBANKCOUNTRYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `BANKCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `BANKBRANCHCODE` | CHAR(6) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `ACCOUNTID` | CHAR(30) | NOT NULL | PK | primary_key |  |
| 6 | `FROMDATE` | DATE | NOT NULL | PK | primary_key | Inclusive start of a validity period. |
| 7 | `TODATE` | DATE |  |  |  | End of a validity period. |
| 8 | `GLCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 9 | `GLCODE` | CHAR(20) |  | FK | foreign_key |  |
| 10 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 11 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 12 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 13 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 14 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 15 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 16 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `BANK_BANK` | `BANKBANKCOUNTRYCODE`, `BANKCODE`, `BANKBRANCHCODE` | [`BANK`](../CORE_MASTER/BANK.md) | `BANKCOUNTRYCODE`, `CODE`, `BRANCHCODE` | RESTRICT | `BANKVSGLMAPPING.BANKBANKCOUNTRYCODE = BANK.BANKCOUNTRYCODE AND BANKVSGLMAPPING.BANKCODE = BANK.CODE AND BANKVSGLMAPPING.BANKBRANCHCODE = BANK.BRANCHCODE` |
| `COMPANYBANK_BANKID` | `COMPANYCODE`, `BANKIDIDENTIFIER` | [`COMPANYBANK`](../CORE_MASTER/COMPANYBANK.md) | `COMPANYCODE`, `IDENTIFIER` | RESTRICT | `BANKVSGLMAPPING.COMPANYCODE = COMPANYBANK.COMPANYCODE AND BANKVSGLMAPPING.BANKIDIDENTIFIER = COMPANYBANK.IDENTIFIER` |
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `BANKVSGLMAPPING.COMPANYCODE = COMPANY.CODE` |
| `GLMASTER_GL` | `GLCOMPANYCODE`, `GLCODE` | [`GLMASTER`](../CORE_MASTER/GLMASTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `BANKVSGLMAPPING.GLCOMPANYCODE = GLMASTER.COMPANYCODE AND BANKVSGLMAPPING.GLCODE = GLMASTER.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `BANKVSGLMAPPINGUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.BANKIDIDENTIFIER,
       t.BANKBANKCOUNTRYCODE,
       t.BANKCODE,
       t.BANKBRANCHCODE,
       t.ACCOUNTID,
       t.FROMDATE,
       t.TODATE,
       t.GLCOMPANYCODE,
       t.GLCODE,
       t.CREATIONDATETIME,
       t.CREATIONUSER
FROM   DB2ADMIN.BANKVSGLMAPPING t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
