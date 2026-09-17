# DB2ADMIN.USACARRIERSHIPMENTIMPORT

- **Module**: `LOCALIZATION` (low confidence — table name starts with 'USA')
- **Roles**: `business_data`
- **Columns**: 21
- **Primary key**: `COMPANYCODE`, `IMPORTTRANSACTIONNUMBER`, `CARRIERREFERENCE`, `REVERSALENTRY`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 107560

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `IMPORTTRANSACTIONNUMBER` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 3 | `CARRIERREFERENCE` | VARCHAR(100) | NOT NULL | PK | primary_key |  |
| 4 | `REVERSALENTRY` | SMALLINT | NOT NULL | PK | primary_key |  |
| 5 | `DOCUMENTREFERENCE` | VARCHAR(100) |  |  |  |  |
| 6 | `REVERSED` | SMALLINT | NOT NULL |  |  |  |
| 7 | `CHARGEVALUE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 8 | `WEIGHTUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 9 | `WEIGHT` | DECIMAL(15,5) |  |  |  |  |
| 10 | `TERMSOFDELIVERYCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 11 | `TERMSOFDELIVERYCODE` | CHAR(3) |  |  |  |  |
| 12 | `TERMSOFSHIPMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 13 | `TERMSOFSHIPMENTCODE` | CHAR(2) |  |  |  |  |
| 14 | `BUSINESSPARTNERNUMBERID` | DECIMAL(8,0) |  |  |  |  |
| 15 | `SDCHARGELINEREF` | VARCHAR(100) |  |  |  |  |
| 16 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 17 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 18 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 19 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 20 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `USACARRIERSHIPMENTIMPORTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.IMPORTSTATUS,
       t.COMPANYCODE,
       t.IMPORTTRANSACTIONNUMBER,
       t.CARRIERREFERENCE,
       t.REVERSALENTRY,
       t.DOCUMENTREFERENCE,
       t.REVERSED,
       t.CHARGEVALUE,
       t.WEIGHTUNITOFMEASURECODE,
       t.WEIGHT,
       t.TERMSOFDELIVERYCOMPANYCODE,
       t.TERMSOFDELIVERYCODE
FROM   DB2ADMIN.USACARRIERSHIPMENTIMPORT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
