# DB2ADMIN.CURRENCYPOOL

- **Module**: `CORE_MASTER` (high confidence — table name starts with 'CURRENCY')
- **Roles**: `business_data`
- **Columns**: 24
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 1 constraint(s), references 5 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 197927

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(15) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `DIVISIONCODE` | CHAR(3) |  | FK | foreign_key | Division within a company; second-level organisational discriminator. |
| 3 | `ORDERCATEGORYORDERTYPE` | CHAR(1) |  | FK | foreign_key |  |
| 4 | `ORDERCATEGORYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 5 | `VALIDITYDATEFROM` | DATE |  |  |  |  |
| 6 | `VALIDITYDATETO` | DATE |  |  |  |  |
| 7 | `CURRENCYCODE` | CHAR(4) |  | FK | foreign_key |  |
| 8 | `FOREIGNAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 9 | `EXTERNALBANKCODE` | CHAR(15) |  | FK | foreign_key |  |
| 10 | `BANKTOWN` | CHAR(100) |  |  |  |  |
| 11 | `BANKEMAIL` | VARCHAR(200) |  |  |  |  |
| 12 | `BANKCONTACT` | VARCHAR(200) |  |  |  |  |
| 13 | `BANKDOCUMENTCODE` | CHAR(50) |  |  |  |  |
| 14 | `RESIDUALAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 15 | `STATUS` | CHAR(1) |  |  |  |  |
| 16 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 17 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 18 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 19 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 20 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 21 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 22 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 23 | `INTERNALNOTE` | VARCHAR(3000) |  |  |  |  |

## References (this table → parent) — 5

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `BANKEXTERNAL_EXTERNALBANK` | `COMPANYCODE`, `EXTERNALBANKCODE` | [`BANKEXTERNAL`](../SALES/BANKEXTERNAL.md) | `COMPANYCODE`, `CODE` | RESTRICT | `CURRENCYPOOL.COMPANYCODE = BANKEXTERNAL.COMPANYCODE AND CURRENCYPOOL.EXTERNALBANKCODE = BANKEXTERNAL.CODE` |
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `CURRENCYPOOL.COMPANYCODE = COMPANY.CODE` |
| `CURRENCY_CURRENCY` | `CURRENCYCODE` | [`CURRENCY`](../CORE_MASTER/CURRENCY.md) | `CODE` | RESTRICT | `CURRENCYPOOL.CURRENCYCODE = CURRENCY.CODE` |
| `DIVISION_DIVISION` | `COMPANYCODE`, `DIVISIONCODE` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `CURRENCYPOOL.COMPANYCODE = DIVISION.COMPANYCODE AND CURRENCYPOOL.DIVISIONCODE = DIVISION.CODE` |
| `ORDERCATEGORY_ORDERCATEGORY` | `COMPANYCODE`, `ORDERCATEGORYORDERTYPE`, `ORDERCATEGORYCODE` | [`ORDERCATEGORY`](../CORE_MASTER/ORDERCATEGORY.md) | `COMPANYCODE`, `ORDERTYPE`, `CODE` | RESTRICT | `CURRENCYPOOL.COMPANYCODE = ORDERCATEGORY.COMPANYCODE AND CURRENCYPOOL.ORDERCATEGORYORDERTYPE = ORDERCATEGORY.ORDERTYPE AND CURRENCYPOOL.ORDERCATEGORYCODE = ORDERCATEGORY.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `CURRENCYPOOL_LINE` | [`CURRENCYPOOLLINE`](../CORE_MASTER/CURRENCYPOOLLINE.md) | `CURRENCYPOOLCOMPANYCODE`, `CURRENCYPOOLCODE` | `CURRENCYPOOLLINE.CURRENCYPOOLCOMPANYCODE = CURRENCYPOOL.COMPANYCODE AND CURRENCYPOOLLINE.CURRENCYPOOLCODE = CURRENCYPOOL.CODE` |

## Indexes

- `CURRENCYPOOLUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.DIVISIONCODE,
       t.ORDERCATEGORYORDERTYPE,
       t.ORDERCATEGORYCODE,
       t.VALIDITYDATEFROM,
       t.VALIDITYDATETO,
       t.CURRENCYCODE,
       t.FOREIGNAMOUNT,
       t.EXTERNALBANKCODE,
       t.BANKTOWN,
       t.BANKEMAIL
FROM   DB2ADMIN.CURRENCYPOOL t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
