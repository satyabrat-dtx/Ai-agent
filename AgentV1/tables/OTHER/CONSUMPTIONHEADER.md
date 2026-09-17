# DB2ADMIN.CONSUMPTIONHEADER

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 26
- **Primary key**: `COMPANYCODE`, `DIVISIONCODE`, `ITEMTYPECODE`, `BUSINESSAREACODE`, `STARTDATE`, `ENDDATE`, `LOGICALWAREHOUSECODE`
- **FK degree**: referenced by 1 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 146588

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FLAG` | CHAR(15) |  |  |  |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL |  | audit |  |
| 3 | `STARTDATE` | DATE | NOT NULL | PK | primary_key |  |
| 4 | `ITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 5 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 6 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK | primary_key | Division within a company; second-level organisational discriminator. |
| 7 | `ENDDATE` | DATE | NOT NULL | PK | primary_key |  |
| 8 | `BUSINESSAREACODE` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 9 | `LOGICALWAREHOUSECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 10 | `LOGICALWAREHOUSECODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 11 | `POSTINGDATE` | DATE | NOT NULL |  |  |  |
| 12 | `SAPMESSAGE` | VARCHAR(500) |  |  |  |  |
| 13 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 14 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 15 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 16 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 17 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 18 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 19 | `FINDOCBUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 20 | `FINDOCFINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 21 | `FINDOCTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 22 | `FINDOCSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 23 | `FINDOCCODE` | CHAR(15) |  |  |  |  |
| 24 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 25 | `OTHFINDOCCODE` | CHAR(15) |  |  |  |  |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `CONSUMPTIONHEADER.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `CONSUMPTIONHEADER_LINE` | [`CONSUMPTIONDETAIL`](../OTHER/CONSUMPTIONDETAIL.md) | `CONSUMPTIONHEADERCOMPANYCODE`, `CONSUMPTIONHEADERDIVISIONCODE`, `CONSUMPTIONHEADERITEMTYPECODE`, `CONSUMPTIONHDRBUSINESSAREACOD`, `CONSUMPTIONHEADERSTARTDATE`, `CONSUMPTIONHEADERENDDATE`, `CONSUMPTIONHDRLGLWHSCODE` | `CONSUMPTIONDETAIL.CONSUMPTIONHEADERCOMPANYCODE = CONSUMPTIONHEADER.COMPANYCODE AND CONSUMPTIONDETAIL.CONSUMPTIONHEADERDIVISIONCODE = CONSUMPTIONHEADER.DIVISIONCODE AND CONSUMPTIONDETAIL.CONSUMPTIONHEADERITEMTYPECODE = CONSUMPTIONHEADER.ITEMTYPECODE AND CONSUMPTIONDETAIL.CONSUMPTIONHDRBUSINESSAREACOD = CONSUMPTIONHEADER.BUSINESSAREACODE AND CONSUMPTIONDETAIL.CONSUMPTIONHEADERSTARTDATE = CONSUMPTIONHEADER.STARTDATE AND CONSUMPTIONDETAIL.CONSUMPTIONHEADERENDDATE = CONSUMPTIONHEADER.ENDDATE AND CONSUMPTIONDETAIL.CONSUMPTIONHDRLGLWHSCODE = CONSUMPTIONHEADER.LOGICALWAREHOUSECODE` |

## Indexes

- `CONSUMPTIONHEADERUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.FLAG,
       t.COMPANYCODE,
       t.CREATIONTIMESTAMP,
       t.STARTDATE,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.DIVISIONCODE,
       t.ENDDATE,
       t.BUSINESSAREACODE,
       t.LOGICALWAREHOUSECOMPANYCODE,
       t.LOGICALWAREHOUSECODE,
       t.POSTINGDATE
FROM   DB2ADMIN.CONSUMPTIONHEADER t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
