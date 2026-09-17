# DB2ADMIN.FINBUYERADVSUBMISSION

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 33
- **Primary key**: `COMPANYCODE`, `ACODE`, `CODE`
- **FK degree**: referenced by 1 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 182348

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `ACODE` | CHAR(5) | NOT NULL | PK | primary_key |  |
| 2 | `SCOUNTERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 3 | `SCODE` | CHAR(15) |  | FK | foreign_key |  |
| 4 | `DOCNO` | CHAR(30) |  |  |  |  |
| 5 | `DOCDATE` | DATE |  |  |  |  |
| 6 | `BUYERCUSTOMERSUPPLIERTYPE` | CHAR(1) |  | FK | foreign_key |  |
| 7 | `BUYERCUSTOMERSUPPLIERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 8 | `CURRENCYSCODE` | CHAR(4) |  | FK | foreign_key |  |
| 9 | `FIRCTYPE` | INTEGER | NOT NULL |  |  |  |
| 10 | `FIRCNO` | CHAR(20) |  |  |  |  |
| 11 | `FIRCDATE` | DATE |  |  |  |  |
| 12 | `FIRCAMT` | DECIMAL(18,5) |  |  |  |  |
| 13 | `INVMODE` | INTEGER | NOT NULL |  |  |  |
| 14 | `TOTALFGNVALUE` | DECIMAL(18,5) |  |  |  |  |
| 15 | `TOTALCCVALUE` | DECIMAL(18,5) |  |  |  |  |
| 16 | `REMARK` | VARCHAR(255) |  |  |  |  |
| 17 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 18 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 19 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 20 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 21 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 22 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 23 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 24 | `CODE` | CHAR(10) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 25 | `EXCHANGEFLUCTUATIONGLCMYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 26 | `EXCHANGEFLUCTUATIONGLCODE` | CHAR(20) |  | FK | foreign_key |  |
| 27 | `POSTINGDATE` | DATE |  |  |  |  |
| 28 | `FINDOCBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 29 | `FINDOCFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 30 | `FINDOCTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 31 | `FINDOCSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 32 | `FINDOCCODE` | CHAR(15) |  |  |  |  |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `CURRENCY_CURRENCYS` | `CURRENCYSCODE` | [`CURRENCY`](../CORE_MASTER/CURRENCY.md) | `CODE` | RESTRICT | `FINBUYERADVSUBMISSION.CURRENCYSCODE = CURRENCY.CODE` |
| `GLMASTER_EXCHANGEFLUCTUATIONGL` | `EXCHANGEFLUCTUATIONGLCMYCODE`, `EXCHANGEFLUCTUATIONGLCODE` | [`GLMASTER`](../CORE_MASTER/GLMASTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FINBUYERADVSUBMISSION.EXCHANGEFLUCTUATIONGLCMYCODE = GLMASTER.COMPANYCODE AND FINBUYERADVSUBMISSION.EXCHANGEFLUCTUATIONGLCODE = GLMASTER.CODE` |
| `ORDERPARTNER_BUYER` | `COMPANYCODE`, `BUYERCUSTOMERSUPPLIERTYPE`, `BUYERCUSTOMERSUPPLIERCODE` | [`ORDERPARTNER`](../CORE_MASTER/ORDERPARTNER.md) | `CUSTOMERSUPPLIERCOMPANYCODE`, `CUSTOMERSUPPLIERTYPE`, `CUSTOMERSUPPLIERCODE` | RESTRICT | `FINBUYERADVSUBMISSION.COMPANYCODE = ORDERPARTNER.CUSTOMERSUPPLIERCOMPANYCODE AND FINBUYERADVSUBMISSION.BUYERCUSTOMERSUPPLIERTYPE = ORDERPARTNER.CUSTOMERSUPPLIERTYPE AND FINBUYERADVSUBMISSION.BUYERCUSTOMERSUPPLIERCODE = ORDERPARTNER.CUSTOMERSUPPLIERCODE` |
| `SALESORDER_S` | `COMPANYCODE`, `SCOUNTERCODE`, `SCODE` | [`SALESORDER`](../SALES/SALESORDER.md) | `COMPANYCODE`, `COUNTERCODE`, `CODE` | RESTRICT | `FINBUYERADVSUBMISSION.COMPANYCODE = SALESORDER.COMPANYCODE AND FINBUYERADVSUBMISSION.SCOUNTERCODE = SALESORDER.COUNTERCODE AND FINBUYERADVSUBMISSION.SCODE = SALESORDER.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `FINBUYERADVSUBMISSION_DETAIL` | [`FINBUYERADVSUBMISSIONDETAIL`](../FINANCE/FINBUYERADVSUBMISSIONDETAIL.md) | `FINBUYERADVSUBMISSIONCMYCODE`, `FINBUYERADVSUBMISSIONACODE`, `FINBUYERADVSUBMISSIONCODE` | `FINBUYERADVSUBMISSIONDETAIL.FINBUYERADVSUBMISSIONCMYCODE = FINBUYERADVSUBMISSION.COMPANYCODE AND FINBUYERADVSUBMISSIONDETAIL.FINBUYERADVSUBMISSIONACODE = FINBUYERADVSUBMISSION.ACODE AND FINBUYERADVSUBMISSIONDETAIL.FINBUYERADVSUBMISSIONCODE = FINBUYERADVSUBMISSION.CODE` |

## Indexes

- `FINBUYERADVSUBMISSIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.ACODE,
       t.SCOUNTERCODE,
       t.SCODE,
       t.DOCNO,
       t.DOCDATE,
       t.BUYERCUSTOMERSUPPLIERTYPE,
       t.BUYERCUSTOMERSUPPLIERCODE,
       t.CURRENCYSCODE,
       t.FIRCTYPE,
       t.FIRCNO,
       t.FIRCDATE
FROM   DB2ADMIN.FINBUYERADVSUBMISSION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
