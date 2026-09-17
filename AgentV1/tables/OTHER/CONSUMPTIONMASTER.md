# DB2ADMIN.CONSUMPTIONMASTER

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 32
- **Primary key**: `COMPANYCODE`, `DIVISIONCODE`, `LOGICALWAREHOUSECODE`, `STARTDATE`, `ENDDATE`, `STOCKTRANSACTIONTEMPLATECODE`, `ITEMTYPECODE`, `BUSINESSAREACODE`, `DEBITGLCODE`, `CREDITGLCODE`, `COSTCENTERCODE`, `BASECOSTUNITCODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 146649

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COUNT` | INTEGER | NOT NULL |  |  |  |
| 1 | `FLAG` | CHAR(15) |  |  |  |  |
| 2 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 3 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL |  | audit |  |
| 4 | `STARTDATE` | DATE | NOT NULL | PK | primary_key |  |
| 5 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK | primary_key | Division within a company; second-level organisational discriminator. |
| 6 | `BASECOSTUNITCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 7 | `ENDDATE` | DATE | NOT NULL | PK | primary_key |  |
| 8 | `CLOSINGBASECOST` | DECIMAL(18,5) |  |  |  |  |
| 9 | `ITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 10 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 11 | `LOGICALWAREHOUSECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 12 | `LOGICALWAREHOUSECODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 13 | `STOCKTRNTEMPLATECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 14 | `STOCKTRANSACTIONTEMPLATECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 15 | `DEBITGLCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 16 | `DEBITGLCODE` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 17 | `CREDITGLCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 18 | `CREDITGLCODE` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 19 | `POSTINGDATE` | DATE | NOT NULL |  |  |  |
| 20 | `SAPMESSAGE` | VARCHAR(500) |  |  |  |  |
| 21 | `BUSINESSAREACODE` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 22 | `QUANTITY` | DECIMAL(18,5) |  |  |  |  |
| 23 | `UOMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 24 | `COSTCENTERCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 25 | `COSTCENTERCODE` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 26 | `FINDOCBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 27 | `FINDOCFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 28 | `FINDOCTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 29 | `FINDOCSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 30 | `FINDOCCODE` | CHAR(15) |  |  |  |  |
| 31 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `CONSUMPTIONMASTER.COMPANYCODE = COMPANY.CODE` |
| `UNITOFMEASURE_UOM` | `UOMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `CONSUMPTIONMASTER.UOMCODE = UNITOFMEASURE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `CONSUMPTIONMASTERUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COUNT,
       t.FLAG,
       t.COMPANYCODE,
       t.CREATIONTIMESTAMP,
       t.STARTDATE,
       t.DIVISIONCODE,
       t.BASECOSTUNITCODE,
       t.ENDDATE,
       t.CLOSINGBASECOST,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.LOGICALWAREHOUSECOMPANYCODE
FROM   DB2ADMIN.CONSUMPTIONMASTER t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
