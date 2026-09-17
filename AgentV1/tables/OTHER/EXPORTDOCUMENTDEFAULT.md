# DB2ADMIN.EXPORTDOCUMENTDEFAULT

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 34
- **Primary key**: `COMPANYCODE`, `DIVISIONCODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 138390

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK | primary_key | Division within a company; second-level organisational discriminator. |
| 2 | `CERTOFORIGIN` | INTEGER | NOT NULL |  |  |  |
| 3 | `GSP` | INTEGER | NOT NULL |  |  |  |
| 4 | `BILLOFLADING` | INTEGER | NOT NULL |  |  |  |
| 5 | `INTIMATIONOFSHIPMENT` | INTEGER | NOT NULL |  |  |  |
| 6 | `AR3` | INTEGER | NOT NULL |  |  |  |
| 7 | `AR4` | INTEGER | NOT NULL |  |  |  |
| 8 | `PMVVALUE` | DECIMAL(9,5) | NOT NULL |  |  |  |
| 9 | `CURRENCYCODE` | CHAR(4) |  | FK | foreign_key |  |
| 10 | `EPCGPERCENTAGEADDNTLCIFVALUE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 11 | `MULTIPLECUSTOMINVOICE` | INTEGER | NOT NULL |  |  |  |
| 12 | `MULTIPLESCHEMETYPE` | INTEGER | NOT NULL |  |  |  |
| 13 | `BANKCERTIFICATETO` | CHAR(100) |  |  |  |  |
| 14 | `INSTCARGOCLSA` | CHAR(50) |  |  |  |  |
| 15 | `INSTCARGOCLSB` | CHAR(50) |  |  |  |  |
| 16 | `INSTCARGOCLSC` | CHAR(50) |  |  |  |  |
| 17 | `INSTWARCLSCARGO` | CHAR(50) |  |  |  |  |
| 18 | `INSTSTRIKECLSCARGO` | CHAR(50) |  |  |  |  |
| 19 | `INSTCARGOCLSAIRCARGO` | CHAR(50) |  |  |  |  |
| 20 | `INSTWARCLSAIRCARGO` | CHAR(50) |  |  |  |  |
| 21 | `INSTSTRIKECLSAIRCARGO` | CHAR(50) |  |  |  |  |
| 22 | `INSTCLASSIFICATIONCLS` | CHAR(50) |  |  |  |  |
| 23 | `INSTRACONTMNCLS` | CHAR(50) |  |  |  |  |
| 24 | `IMPNOTICE` | CHAR(50) |  |  |  |  |
| 25 | `BOEHL1` | CHAR(50) |  |  |  |  |
| 26 | `BOEHL2` | CHAR(50) |  |  |  |  |
| 27 | `BOEHL3` | CHAR(50) |  |  |  |  |
| 28 | `BOEHL4` | CHAR(50) |  |  |  |  |
| 29 | `BOEHL5` | CHAR(50) |  |  |  |  |
| 30 | `MINIMUMEDIPOSTINGVALUE` | DECIMAL(18,5) |  |  |  |  |
| 31 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 32 | `BILLOFEXCHANGELOGMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 33 | `MINIMUMROBPOSTINGVALUE` | DECIMAL(18,5) |  |  |  |  |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `EXPORTDOCUMENTDEFAULT.COMPANYCODE = COMPANY.CODE` |
| `CURRENCY_CURRENCY` | `CURRENCYCODE` | [`CURRENCY`](../CORE_MASTER/CURRENCY.md) | `CODE` | RESTRICT | `EXPORTDOCUMENTDEFAULT.CURRENCYCODE = CURRENCY.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `EXPORTDOCUMENTDEFAULTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.CERTOFORIGIN,
       t.GSP,
       t.BILLOFLADING,
       t.INTIMATIONOFSHIPMENT,
       t.AR3,
       t.AR4,
       t.PMVVALUE,
       t.CURRENCYCODE,
       t.EPCGPERCENTAGEADDNTLCIFVALUE,
       t.MULTIPLECUSTOMINVOICE
FROM   DB2ADMIN.EXPORTDOCUMENTDEFAULT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
