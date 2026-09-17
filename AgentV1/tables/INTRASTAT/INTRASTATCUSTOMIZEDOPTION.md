# DB2ADMIN.INTRASTATCUSTOMIZEDOPTION

- **Module**: `INTRASTAT` (high confidence — table name starts with 'INTRASTAT')
- **Roles**: `business_data`
- **Columns**: 24
- **Primary key**: `COMPANYCODE`
- **FK degree**: referenced by 1 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 23253

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `PURCHASESPERIOD` | CHAR(1) | NOT NULL |  |  |  |
| 2 | `SALESPERIOD` | CHAR(1) | NOT NULL |  |  |  |
| 3 | `DECLARATIONONDISK` | SMALLINT | NOT NULL |  |  |  |
| 4 | `CONTEMPORARYTRANSACTION` | CHAR(1) | NOT NULL |  |  |  |
| 5 | `BATCHUMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 6 | `PURCHASESSTATISTICAMOUNT` | SMALLINT | NOT NULL |  |  |  |
| 7 | `SALESSTATISTICAMOUNT` | SMALLINT | NOT NULL |  |  |  |
| 8 | `PURCHASESFORSTATISTIC` | SMALLINT | NOT NULL |  |  |  |
| 9 | `SALESFORSTATISTIC` | SMALLINT | NOT NULL |  |  |  |
| 10 | `DECLARERADDRESSUNIQUEID` | BIGINT | NOT NULL | FK | foreign_key |  |
| 11 | `DECLARERADDRESSCODE` | CHAR(8) |  | FK | foreign_key |  |
| 12 | `INTRASTATTRANSACTIONPOLICYCODE` | CHAR(20) |  |  |  |  |
| 13 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 14 | `MULTICOUNTRY` | SMALLINT | NOT NULL |  |  |  |
| 15 | `PURCHASESFORFISCAL` | SMALLINT | NOT NULL |  |  |  |
| 16 | `SALESFORFISCAL` | SMALLINT | NOT NULL |  |  |  |
| 17 | `INTRASTATDECLARATIONPOLICYCODE` | CHAR(20) |  |  |  |  |
| 18 | `CODEONREGISTERLENGTH` | INTEGER | NOT NULL |  |  |  |
| 19 | `FILLNATUREB` | SMALLINT | NOT NULL |  |  |  |
| 20 | `CUSTOMCODE` | CHAR(6) |  |  |  |  |
| 21 | `THIRDPARTYDECLARANT` | SMALLINT | NOT NULL |  |  |  |
| 22 | `THIRDPARTYTAXREGNUM` | CHAR(15) |  |  |  |  |
| 23 | `FILEPATH` | VARCHAR(250) | NOT NULL |  |  |  |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ADDRESS_DECLARERADDRESS` | `DECLARERADDRESSUNIQUEID`, `DECLARERADDRESSCODE` | [`ADDRESS`](../CORE_MASTER/ADDRESS.md) | `UNIQUEID`, `CODE` | RESTRICT | `INTRASTATCUSTOMIZEDOPTION.DECLARERADDRESSUNIQUEID = ADDRESS.UNIQUEID AND INTRASTATCUSTOMIZEDOPTION.DECLARERADDRESSCODE = ADDRESS.CODE` |
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `INTRASTATCUSTOMIZEDOPTION.COMPANYCODE = COMPANY.CODE` |
| `UNITOFMEASURE_BATCHUM` | `BATCHUMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `INTRASTATCUSTOMIZEDOPTION.BATCHUMCODE = UNITOFMEASURE.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `INTRASTATCUSTOMIZEDOPTION_COUNTRIES` | [`INTRASTATCUSTOMIZEDOPTBYCOU`](../INTRASTAT/INTRASTATCUSTOMIZEDOPTBYCOU.md) | `INTRASTATCUSTOMIZEDOPTCMPCOD` | `INTRASTATCUSTOMIZEDOPTBYCOU.INTRASTATCUSTOMIZEDOPTCMPCOD = INTRASTATCUSTOMIZEDOPTION.COMPANYCODE` |

## Indexes

- `INTRASTATCUSTOMIZEDOPTIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.PURCHASESPERIOD,
       t.SALESPERIOD,
       t.DECLARATIONONDISK,
       t.CONTEMPORARYTRANSACTION,
       t.BATCHUMCODE,
       t.PURCHASESSTATISTICAMOUNT,
       t.SALESSTATISTICAMOUNT,
       t.PURCHASESFORSTATISTIC,
       t.SALESFORSTATISTIC,
       t.DECLARERADDRESSUNIQUEID,
       t.DECLARERADDRESSCODE
FROM   DB2ADMIN.INTRASTATCUSTOMIZEDOPTION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
